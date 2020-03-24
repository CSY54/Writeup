# [Rev] Masochistic Sudoku

> Points: 160
> Solves: 100

## Description

Clam's tired of the ease and boredom of traditional sudoku. Having just one solution that can be determined via a simple online sudoku solver isn't good enough for him. So, he made [masochistic sudoku](masochistic_sudoku)! Since there are no hints, there are around 6*10^21 possible solutions but only one is actually accepted!

Find it on the shell server at `/problems/2020/masochistic_sudoku/`.

## Solution

This is a sudoku game.

**initial state of the board**

The program checked some blocks by using the number of the block as the seed and call `random()`, comparing the value with the hardcoded value.

After reversing these blocks, we can get:

```
1 0 0 0 6 0 8 5 0
0 0 5 0 8 3 1 0 0
0 0 0 0 1 2 0 9 0
9 0 7 0 0 0 0 0 0
5 3 0 0 0 0 0 8 9
0 0 0 0 0 0 3 0 5
0 4 0 6 2 0 0 0 0
0 0 6 1 9 0 7 0 0
0 2 1 0 3 0 0 0 4
```
(`0`: unknown)

**z3**

We can use z3 to solve the sudoku.

[solve.py](solve.py)

Flag `actf{sud0ku_but_f0r_pe0ple_wh0_h4te_th3mselves}`
