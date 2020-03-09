# [Forensics] Observe Closely - (50 pts)

## Description

A simple image with a couple of twists...

by phleisch

## Solution

There is a zip file hidden behind the image.

```sh
$ binwalk Griffith_Observatory.png
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 320 x 155, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, default compression
127759        0x1F30F         Zip archive data, at least v2.0 to extract, compressed size: 2587, uncompressed size: 16664, name: hidden_binary
130500        0x1FDC4         End of Zip archive

$ dd if=Griffith_Observatory.png of=hidden_binary.zip bs=1 skip=127759
2763+0 records in
2763+0 records out
2763 bytes transferred in 0.015218 secs (181561 bytes/sec)

$ unzip hidden_binary.zip
Archive:  hidden_binary.zip
  inflating: hidden_binary

$ ./hidden_binary
Ah, you found me!
utflag{2fbe9adc2ad89c71da48cabe90a121c0}
```

Flag `utflag{2fbe9adc2ad89c71da48cabe90a121c0}`
