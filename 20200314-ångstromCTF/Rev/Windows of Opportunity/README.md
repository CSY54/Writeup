# [Rev] Windows of Opportunity

> Points: 50
> Solves: 789

## Description

Clam's a windows elitist and he just can't stand seeing all of these linux challenges! So, he decided to step in and create his [own rev challenge](windows_of_opportunity.exe) with the "superior" operating system.

> Hint: You can probably solve it just by looking at the disassembly.

## Solution

```sh
$ strings windows_of_opportunity.exe | grep -o "actf{.*}"
actf{ok4y_m4yb3_linux_is_s7ill_b3tt3r}
```

Flag `actf{ok4y_m4yb3_linux_is_s7ill_b3tt3r}`
