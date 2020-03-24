from PIL import Image

img1 = Image.open('breathe.jpg')
img2 = Image.open('output.png')
assert(img1.size == img2.size)

W, H = img1.size

def dec(a, b):
    a = str(a)
    b = str(b).zfill(len(a))
    if b == '255':
        return '?'
    return b[0]

def get(n):
    if '?' in n:
        return '?'
    return chr(int(n))

def parse(s):
    res = ''
    i = 0
    while i < len(s):
        if s[i] == '1':
            res += get(s[i:i + 3])
            i += 3
        else:
            res += get(s[i:i + 2])
            i += 2
    return res

res = ''
for j in range(H):
    for i in range(W):
        data1 = img1.getpixel((i, j))
        data2 = img2.getpixel((i, j))
        for a, b in zip(data1, data2):
            res += dec(a, b)

print(parse(res))


