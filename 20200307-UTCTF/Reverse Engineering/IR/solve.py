s = '\x03\x12\x1A\x17\x0A\xEC\xF2\x14\x0E\x05\x03\x1D\x19\x0E\x02\x0A\x1F\x07\x0C\x01\x17\x06\x0C\x0A\x19\x13\x0A\x16\x1C\x18\x08\x07\x1A\x03\x1D\x1C\x11\x0B\xF3\x87\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05'

s = [ord(i) for i in s]

for i in range(len(s) - 1, 0, -1):
    s[i - 1] ^= s[i]

s = [i - 5 for i in s]
print(''.join(chr(i) for i in s))
