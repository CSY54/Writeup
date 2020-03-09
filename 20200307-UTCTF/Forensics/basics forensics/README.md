# [Forensics] [basics] forensics - (50 pts)

## Description

My friend said they hid a flag in this picture, but it's broken! Now that I think about it, I don't even know if it really is a picture...

_by balex_

## Solution

It's actually a text file.

```sh
$ grep 'utflag{.*}' secret.jpeg
utflag{fil3_ext3nsi0ns_4r3nt_r34l}
```

Flag `utflag{fil3_ext3nsi0ns_4r3nt_r34l}`
