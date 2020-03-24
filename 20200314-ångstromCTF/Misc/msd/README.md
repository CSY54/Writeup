# [Misc] msd

> Points: 140
> Solves: 203

## Description

You thought Angstrom would have a stereotypical LSB challenge...
You were wrong!
To spice it up, we're now using the [Most Significant Digit](public.py). Can you still power through it?

Here's the [encoded image](output.png), and here's the [original image](breathe.jpg), for the... well, you'll see.

Important: Redownload the image if you have one from before 11:30 AM 3/14/20.
Important: Don't use Python 3.8, use an older version of Python 3!

> Hint: Look at the difference between the original and what I created!
> Also, which way does LSB work?

## Solution

The script replace the most significant digit (in decimal) of the pixel value with the flag digit one by one.

e.g.
```
(original value) -- (flag digit) --> (result value)
20 -- 3 --> 30
255 -- 1 --> 155
```

However, there is something need to be mentioned:

```
120 -- 3 --> 255
123 -- 9 --> 255
```

If the pixel is encoded with the exception mentioned above, we cannot recover the original value from it.

In my solve script, I use `?` to represent such case.

```sh
$ python solve.py | grep -oE "actf{[^?}]*}"
actf{inhale_exhale_ezpz-12309biggyhaby}
actf{inhale_exhale_ezpz-12309biggyhaby}
```

Flag `actf{inhale_exhale_ezpz-12309biggyhaby}`
