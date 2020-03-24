from Crypto.Util.number import long_to_bytes
from string import printable

c1 = 'artomtf2srn00tgm2f'
c2 = 'ng0fa0mat0tmmmra0c'
c3 = 'ngnrmcornttnsmgcgr'
c4 = 'a0fn2rfa00tcgctaot'

basechars = 'angstromctf20'

def _tobase(s):
    ret = [0]
    for ch in s:
        if ch == 't':
            for i in range(len(ret)):
                ret[i] *= 13
                ret.append(ret[i] + 4)
                ret[i] += 9
        else:
            for i in range(len(ret)):
                ret[i] *= 13
                ret[i] += basechars.index(ch)
    return ret
    
def tostr(lst):
    ret = []
    for _ in lst:
        tmp = long_to_bytes(_)
        if all(ch in printable for ch in tmp):
            ret.append(tmp)
    return ret

n1 = _tobase(c1)
s1 = tostr(n1)
assert(len(s1) == 1)
res1 = s1[0]

n2 = _tobase(c2)
for _ in range(len(n2)):
    n2[_] = (1 << 64) - 1 - n2[_]
s2 = tostr(n2)
assert(len(s2) == 1)
res2 = s2[0]

n3 = _tobase(c3)
for _ in range(len(n3)):
    n3[_] = (1 << 64) - (n3[_] - 0x1337)
s3 = tostr(n3)
assert(len(s3) == 1)
res3 = s3[0]

n4 = _tobase(c4)
for _ in range(len(n4)):
    n4[_] = (n4[_] + 0x4242) ^ 0x1234567890abcdef
res4 = tostr(n4)

fhalf = res1[::-1] + res2[::-1]

for _ in res4:
    shalf = res3[::-1] + _[::-1]
    assert(len(fhalf) == len(shalf))
    inp = ''.join(i + j for i, j in zip(fhalf, shalf))
    print(inp)
