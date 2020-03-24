# [Web] Woooosh

> Points: 130
> Solves: 184

## Description

Clam's tired of people hacking his sites so he spammed obfuscation on his [new game](https://woooosh.2020.chall.actf.co). I have a feeling that behind that wall of obfuscated javascript there's still a vulnerable site though. Can you get enough points to get the flag? I also found the [backend source](index.js).

Second instance: [https://wooooosh.2020.chall.actf.co/](https://wooooosh.2020.chall.actf.co/)

> Hint: The frontend is obfuscated but maybe something else isn't?

## Solution

After reviewing the code, I thought it was something about race condition.

So my teammate wrote [solve.js](solve.js) to send 20 request to the server in a row.

Then, we get the flag!

Flag `actf{w0000sh_1s_th3_s0und_0f_th3_r3qu3st_fly1ng_p4st_th3_fr0nt3nd}`
