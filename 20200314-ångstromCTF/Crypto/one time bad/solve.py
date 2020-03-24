from pwn import *
import random, time
import string
from base64 import b64decode

def otp(a, b):
    r = ''
    for i, j in zip(a, b):
        r += chr(ord(i) ^ ord(j))
    return r

def genSample():
	p = ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for _ in range(random.randint(1, 30))])
	k = ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for _ in range(len(p))])

	x = otp(p, k)

	return x, p, k

HOST, PORT = 'misc.2020.chall.actf.co', 20301

r = remote(HOST, PORT)
_seed = int(time.time())

r.sendlineafter('> ', '1')
res = r.recvline().strip().decode().split(' ')
x = b64decode(res[0].encode()).decode()
k = b64decode(res[3].encode()).decode()

for i in range(-5, 5):
    random.seed(_seed + i)
    _x, _p, _k = genSample()
    if _x == x and _k == k:
        _seed = _seed + i
        print('ok, offset = {}'.format(i))
        break

random.seed(_seed)
genSample()
_x, _p, _k = genSample()

r.sendlineafter('> ', '2')
r.sendline(_p)
r.interactive()

'''
actf{one_time_pad_more_like_i_dont_like_crypto-1982309}
'''
