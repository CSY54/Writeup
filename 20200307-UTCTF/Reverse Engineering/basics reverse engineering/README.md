# [Reverse Engineering] [basics] reverse engineering - (50 pts)

## Description

I know there's a string in this binary somewhere.... Now where did I leave it?

_by balex_

## Solution

```sh
$ strings calc | grep 'utflag{.*}' 
utflag{str1ngs_1s_y0ur_fr13nd}
```

Flag `utflag{str1ngs_1s_y0ur_fr13nd}`
