# [Rev] Revving Up

> Points: 50
> Solves: 945

## Description

Clam wrote [a program](revving_up) for his school's cybersecurity club's first rev lecture! Can you get it to give you the flag? You can find it at `/problems/2020/revving_up` on the shell server, which you can access via the "shell" link at the top of the site.

> Hint: Try some google searches for "how to run a file in linux" or "bash for beginners".

## Solution

```python
from pwn import *

with open('../../.ssh', 'r') as f:
    host = f.readline().strip()
    user = f.readline().strip()
    password = f.readline().strip()

sh = ssh(host=host, user=user, password=password)

sh.set_working_directory('/problems/2020/revving_up/')

r = sh.run(['./revving_up', 'banana'])

r.sendline('give flag')

r.interactive()
```

Flag `actf{g3tting_4_h4ng_0f_l1nux_4nd_b4sh}`
