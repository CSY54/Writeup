from string import ascii_lowercase

CHARSET = ascii_lowercase

def gen():
    for i in range(len(CHARSET)):
        for j in range(len(CHARSET)):
            for k in range(len(CHARSET)):
                for l in range(len(CHARSET)):
                    yield [[i, j], [k, l]]

def to_val(ch):
    return CHARSET.index(ch)

def to_char(val):
    return CHARSET[val]

def enc(pt, key):
    pt = [[to_val(i)] for i in pt]
    ct = [[0] for i in range(len(pt))]

    for i in range(len(key)):
        for j in range(len(pt[0])):
            for k in range(len(key[0])):
                ct[i][j] = (ct[i][j] + key[i][k] * pt[k][j]) % len(CHARSET)

    return ''.join(to_char(i[0]) for i in ct)

ct = 'wznqca{d4uqop0fk_q1nwofdbzg_eu}'
filtered_ct = ''.join(i if i in CHARSET else '' for i in ct)

key = [[1, 22], [11, 13]]
k = inverse(1 * 13 - 22 * 11, len(CHARSET))
rkey = [
    [(13 * k) % len(CHARSET), (-22 * k) % len(CHARSET)], 
    [(-11 * k) % len(CHARSET), (1 * k) % len(CHARSET)]
]

pt = ''.join(enc(filtered_ct[i:i + 2], key) for i in range(0, len(filtered_ct), 2))

flag = ''
pid = 0
for i in ct:
    if i in CHARSET:
        flag += pt[pid]
        pid += 1
    else:
        flag += i
        
print(flag)
assert(flag == 'utflag{d4nger0us_c1phertext_qq}')

'''
pair = {
    'ut': 'wz',
    'fl': 'nq',
    'ag': 'ca',
}

keygen = gen()

while True:
    key = next(keygen)
    cnt = 0

    for pt, ct in pair.items():
        if enc(pt, key) != ct:
            break
        cnt += 1

    if cnt == 3:
        print(key)
'''
