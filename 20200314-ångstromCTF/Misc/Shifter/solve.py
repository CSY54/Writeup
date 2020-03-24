from pwn import *
from string import ascii_uppercase

HOST, PORT = 'misc.2020.chall.actf.co', 20300

fib = [0, 1, 1]
while len(fib) < 50:
    fib.append((fib[-1] + fib[-2]) % 26)

r = remote(HOST, PORT)
r.recvlines(6)

for i in range(50):
    task = r.recvline().strip().split(' ')
    p = task[1]
    n = int(task[3].split('=')[1])
    res = ''.join(ascii_uppercase[(ascii_uppercase.index(i) + fib[n]) % 26] for i in p)
    r.sendlineafter(': ', res)

r.interactive()

'''
actf{h0p3_y0u_us3d_th3_f0rmu14-1985098}
'''
