# [Web] Defund's Crypt

> Points: 120
> Solves: 318

## Description

One year since defund's descent. One crypt. One void to fill. Clam must do it, [and so must you.](https://crypt.2020.chall.actf.co)

> Hint: Who says images can't identify as more than one thing? This is 2020.

## Solution

Head over to `https://crypt.2020.chall.actf.co/src.php` to get the source.

The image we uploaded must follow the rules:

- Filename contains `.jpg` or `.png` or `.bmp`
- MIME type is same with the extension.

We can bypass the first rule by naming the file `xxx.png.php`.

As for the second rule, we can append the php code to an existing png file (since the MIME must match the extension).

![](Screenshot.png)

Flag `actf{th3_ch4ll3ng3_h4s_f4ll3n_but_th3_crypt_rem4ins}`
