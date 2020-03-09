# [Cryptography] Hill - (89 pts)

## Description

I found these characters on top of a hill covered with algae ... bruh I can't figure it out can you help me?

```wznqca{d4uqop0fk_q1nwofDbzg_eu}```

by bnuno

## Solution

since we know the flag format is `utflag{}`, we can brute force the key such that

```txt
encrypt('ut', key) = 'wz'
encrypt('fl', key) = 'nq'
encrypt('ag', key) = 'ca'
```

```python
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
```

There are only one key satisfies the constraints `[[1, 22], [11, 13]]`.

By decrypting the given ciphertext, we can get the flag.

Flag `utflag{d4nger0us_c1phertext_qq}`
