# [Misc] ws1

> Points: 30
> Solves: 1266

## Description

Find my password from [this recording](recording.pcapng) (:

## Solution

```sh
$ strings recording.pcapng | grep -o "actf{.*}"
actf{wireshark_isn't_so_bad_huh-a9d8g99ikdf}
```

Flag `actf{wireshark_isn't_so_bad_huh-a9d8g99ikdf}`
