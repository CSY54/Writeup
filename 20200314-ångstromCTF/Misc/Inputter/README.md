# [Misc] Inputter

> Points: 100
> Solves: 385

## Description

Clam **really** likes challenging himself. When he learned about all these weird unprintable ASCII characters he just HAD to put it in [a challenge](inputter). Can you satisfy his knack for strange and hard-to-input characters? [Source.](inputter.c)

Find it on the shell server at `/problems/2020/inputter/`.

> Hint: There are ways to run programs without using the shell.

## Solution

This challenge provides the source of the program.

We need to pass ` \n'"\x07` as the argument when starting the program.
Also, input `\x00\x01\x02\x03\n` for the second comparison.

We can achieve this by using pwntools.

[solve.py](solve.py)

Flag `actf{impr4ctic4l_pr0blems_c4ll_f0r_impr4ctic4l_s0lutions}`
