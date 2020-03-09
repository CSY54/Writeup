# [Forensics] The Legend of Hackerman, Pt. 1 - (50 pts)

## Description

My friend Hackerman tried to send me a secret transmission, but I think some of it got messed up in transit. Can you fix it?

_by balex_

## Solution

The file should be a PNG file, but the header is missing.

```sh
$ xxd hackerman.png | head
00000000: 0000 0000 0d0a 1a0a 0000 000d 4948 4452  ............IHDR
00000010: 0000 04a8 0000 029e 0806 0000 0081 2e23  ...............#
00000020: af00 0028 257a 5458 7452 6177 2070 726f  ...(%zTXtRaw pro
00000030: 6669 6c65 2074 7970 6520 6578 6966 0000  file type exif..
00000040: 78da ad9c 6992 1c37 9285 ffe3 1473 04ec  x...i..7.....s..
00000050: cb71 e058 cce6 067d fcf9 1e32 4991 92ba  .q.X...}...2I...
00000060: a7db ac45 1349 5565 4520 e0ee 6f71 78c8  ...E.IUeE ..oqx.
00000070: 9d7f fcef 75ff c33f 2394 ec72 69bd 8e5a  ....u..?#..ri..Z
00000080: 3dff e491 479c fca5 fbcf 3fe3 fd1e 7c7e  =...G.....?...|~
00000090: bfbf 7f66 7fff a5ff feed eb6e 1c1f dfdf  ...f.......n....
```

By modifying the leading 4 bytes into `89 50 4e 47`, which is the PNG header, it'll be able to open.

Flag `utflag{3lit3_h4ck3r}`
