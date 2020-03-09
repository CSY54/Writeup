# [Reverse Engineering] .PNG2 - (50 pts)

## Description

In an effort to get rid of all of the bloat in the .png format, I'm proud to announce .PNG2! The first pixel is #7F7F7F, can you get the rest of the image?

by bnuno

## Solution

The file contains the color code in hex for each pixel of the original image.

We can use PIL(Python Image Library) to parse it back easily.

![](res.png)

Flag `utflag{j139adfo_93u12hfaj}`
