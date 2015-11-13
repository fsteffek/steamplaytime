SteamPlog
=============

SteamPlog logs and plots your in-game time for your steam games.

Note: SteamPlog is not endorsed, sponsored, affiliated with or otherwise authorized by Valve Corporation.

![Steamplog Q1-2015](https://photos-5.dropbox.com/t/2/AAAPogR-i9_c0QAt3mo0fWJZP7XAu0Md-blUTC8f6S67hQ/12/30030600/png/32x32/1/1445097600/0/2/4_56662202161037332.png/CIj2qA4gASACIAMgBSAHKAEoAigH/DX2qWn4daAbcSErhP6814FFP3pkuwpcP-GMFZ4yJXik?size=1024x768&size_mode=2)

### Getting Started

#### Requirements
* [Steam API Key](http://steamcommunity.com/dev) ([Powered by Steam](http://steampowered.com))
* Python 2.7.6+ (lower versions untested)
* `sqlite3`
* `python-matplotlib`

#### First time setup

The first time you run `steamplog.py`, the file `config.json` is created. You need to add your API key and Steam ID to `config.json`. After that you may run the following commands:

```bash
$ ./steamplog.py log                # run it once a day at the same time
$ ./steamplog.py plot               # run whenever you want
...
$ ./steamplog.py plot -lc -o 2015-Q3 2015-07-01 2015-09-30
```

Run with option `-h` to see all available options.

```
$ ./steamplog.py -h
steamplog - log and plot your steam gaming time

usage:
  steamplog.py log [<DATE>]
  steamplog.py plot [<DATE_FROM> [<DATE_TO>]]
                    [-lc] [-o FILE] [-v]
  steamplog.py stats [--full]

plot options:
  [<DATE_FROM>]     include every playtime from this date (format: YYYY-MM-DD)
                    [default: last 14 days]
  [<DATE_TO>]       include every playtime from this date (format: YYYY-MM-DD)
                    [default: today]
  -c, --color       top 10 games have different colors
  -l, --legend      include a legend
  -o FILENAME, --output FILENAME
                    FILENAME of the output image without extension

stats options:
  --full            print every game

other:
  -v, --verbose  be verbose
  -h, --help     show this help
```

### Automating

#### On Linux

Edit your [crontab](https://github.com/fsteffek/steamplog/wiki/Automation-%28set-and-forget%29)

#### On Windows

Use the task sheduler

