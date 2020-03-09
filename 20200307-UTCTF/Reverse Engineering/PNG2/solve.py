from PIL import Image

data = open('pic.png2', 'r').read()[21:]
W, H = 0x05cf, 0x0288

img = Image.new('RGBA', (W, H))
pix = img.load()

id = 0
for i in range(H):
    for j in range(W):
        R = ord(data[id])
        G = ord(data[id + 1])
        B = ord(data[id + 2])
        id += 3
        pix[j, i] = (R, G, B, 0xff)

img.save('res.png')



