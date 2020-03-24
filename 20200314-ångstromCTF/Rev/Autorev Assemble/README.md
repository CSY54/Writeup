# [Rev] Autorev, Assemble!

> Points: 125
> Solves: 250

## Description

Clam was trying to make a neural network to automatically do reverse engineering for him, but he made a typo and the neural net ended up making a reverse engineering challenge instead of solving one! Can you [get the flag?](autorev_assemble)

Find it on the shell server at `/problems/2020/autorev_assemble/` or over tcp at `nc shell.actf.co 20203`.

> Hint: Don't do this by hand.

## Solution

Just a glance of the decompiled code, I fired up angr immediately.

```python
import angr

p = angr.Project('./autorev_assemble')
state = p.factory.entry_state(args=['./autorev_assemble'])
sm = p.factory.simgr(state)
sm.explore(find=0x40894c, avoid=0x40895a)

print(sm.found[0].posix.dumps(0))
```

Flag `actf{wr0t3_4_pr0gr4m_t0_h3lp_y0u_w1th_th1s_df93171eb49e21a3a436e186bc68a5b2d8ed}`
