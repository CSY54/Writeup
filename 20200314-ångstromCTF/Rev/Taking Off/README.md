# [Rev] Taking Off

> Points: 70
> Solves: 522

## Description

So you started revving up, but is it enough to [take off](taking_off)? Find the problem in `/problems/2020/taking_off/` in the shell server.

> Hint: You should look into tools like GHIDRA, `gdb`, and `objdump`.

## Solution

```python
from pwn import *

with open('../../.ssh', 'r') as f:
    host = f.readline().strip()
    user = f.readline().strip()
    password = f.readline().strip()

sh = ssh(host=host, user=user, password=password)

sh.set_working_directory('/problems/2020/taking_off/')

r = sh.run(['./taking_off', '3', '9', '2', 'chicken'])

desired = [0x5A, 0x46, 0x4F, 0x4B, 0x59, 0x4F, 0x0A, 0x4D, 0x43, 0x5C, 0x4F, 0x0A, 0x4C, 0x46, 0x4B, 0x4D, 0x2A]

r.sendline(''.join(chr(i ^ 0x2A) for i in desired))

r.interactive()
```

Flag `actf{th3y_gr0w_up_s0_f4st}`
