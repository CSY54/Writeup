from pwn import *

with open('../../.ssh', 'r') as f:
    host = f.readline().strip()
    user = f.readline().strip()
    password = f.readline().strip()

sh = ssh(host=host, user=user, password=password)

sh.set_working_directory('/problems/2020/inputter/')

r = sh.run(['./inputter', " \n'\"\x07"])

r.sendline('\x00\x01\x02\x03\n')

r.interactive()

'''
actf{impr4ctic4l_pr0blems_c4ll_f0r_impr4ctic4l_s0lutions}
'''
