# [Crypto] one time bad

> Points: 100
> Solves: 262

## Description

My super secure service is available now!

Heck, even with [the source](server.py), I bet you won't figure it out.

`nc misc.2020.chall.actf.co 20301`

## Solution

It's using `int(time.time())` as the seed of the random number generator.

We can obtain the same result as the server if our seed is equal to the one on the server.

[solve.py](solve.py)

Flag `actf{one_time_pad_more_like_i_dont_like_crypto-1982309}`
