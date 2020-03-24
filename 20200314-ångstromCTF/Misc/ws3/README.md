# [Misc] ws3

> Points: 180
> Solves: 282

## Description

What the...
[record.pcapng](record.pcapng)

> Hint: Did I *send* something? Or...

## Solution

It's interacting with the server using git services.

After digging into the packet, we can see `0000PACK`, which is the format of the git packfile.

By extracting those packets and follow the instructions in [this post](http://ctf.publog.jp/archives/1056965923.html), we can recover the structure as below:

```
.
└── .git
    ├── HEAD
    ├── config
    ├── description
    ├── hooks
    │   ├── applypatch-msg.sample
    │   ├── commit-msg.sample
    │   ├── fsmonitor-watchman.sample
    │   ├── post-update.sample
    │   ├── pre-applypatch.sample
    │   ├── pre-commit.sample
    │   ├── pre-push.sample
    │   ├── pre-rebase.sample
    │   ├── pre-receive.sample
    │   ├── prepare-commit-msg.sample
    │   └── update.sample
    ├── info
    │   └── exclude
    ├── objects
    │   ├── 0f
    │   │   └── 2f9c092a89bb896f573506300393327aeb8dd2
    │   ├── 34
    │   │   └── b1647544bdcf0e896e080ec84bb8b57cccc8d0
    │   ├── 87
    │   │   └── 872f28963e229e8271e0fab6a557a1e5fb5131
    │   ├── a1
    │   │   └── ec825e60819302795b5e33e92be08bfcd1885e
    │   ├── fe
    │   │   └── 3f47cbcb3ad8e946d0aad59259bdb1bc9e63f2
    │   ├── info
    │   └── pack
    └── refs
        ├── heads
        └── tags

14 directories, 20 files
```

We can use `git cat-file -p <folder_name + file_name>` to get the content.

```sh
$ git cat-file -p fe3f47cbcb3ad8e946d0aad59259bdb1bc9e63f2
JFIF[...]

$ git cat-file -p fe3f47cbcb3ad8e946d0aad59259bdb1bc9e63f2 > flag.jpg
```

![](flag.jpg)

Flag `actf{git_good_git_wireshark-123323}`
