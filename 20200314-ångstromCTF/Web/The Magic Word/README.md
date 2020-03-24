# [Web] The Magic Word

> Points: 20
> Solves: 1357

## Description

[Ask and you shall receive](https://magicword.2020.chall.actf.co)...that is as long as you use the magic word.

> Hint: Change "give flag" to "please give flag" somehow.

## Solution

The script:

```javascript
var msg = document.getElementById("magic");
setInterval(function() {
    if (magic.innerText == "please give flag") {
        fetch("/flag?msg=" + encodeURIComponent(msg.innerText))
            .then(res => res.text())
            .then(txt => magic.innerText = txt.split``.map(v => String.fromCharCode(v.charCodeAt(0) ^ 0xf)).join``);
    }
}, 1000);
```

Just modify the text into `please give flag` to receive flag.

Flag `actf{1nsp3c7_3l3m3nt_is_y0ur_b3st_fri3nd}`
