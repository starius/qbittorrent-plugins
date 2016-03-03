# qBittorrent plugins

## How to use

Run qBittorrent, enable search plugins and add this file.
It may work slowly.

See [the list of unofficial search plugins][1].

[1]: https://github.com/qbittorrent/qBittorrent/wiki/Unofficial-search-plugins

## How to test (for developers)

 1. Read [How to write a search plugin][2].
 2. Clone qBittorrent tree using
    `git clone https://github.com/qbittorrent/qBittorrent`.
 3. Apply [the patch](https://gist.github.com/1a295e1cfceaa676ac5f).
 4. Copy file `tfile_me.py` to directories
    `qBittorrent/src/searchengine/nova` (for Python 2) and
    `qBittorrent/src/searchengine/nova3` (for Python 3).
 5. Run it.

Python 2:

```
$ cd qBittorrent/src/searchengine/nova
$ python2 nova2.py tfile_me all test
```

Python 3:

```
$ cd qBittorrent/src/searchengine/nova3
$ python3 nova2.py tfile_me all test
```
[2]: https://github.com/qbittorrent/qBittorrent/wiki/How-to-write-a-search-plugin
