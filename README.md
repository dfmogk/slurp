slurp.py
========
Gets a random image from deviantart, based on a search string.

<h3>Usage</h3>

Usage: `$ python slurp.py [random/first/last] "Search String" "savedir"`
(Note: `savedir` is optional)

* `random` gets a random image from the first search page.
* `first` gets the first image from the search page.
* `last` gets the last image from the search page.

slurp.py prints the link to the raw image, and, if `savedir` is set, saves the image there.

<h3>Example</h3>
Three examples showing the different modes:
* `python3 slurp.py random "Oak Snow Road"`
* `python3 slurp.py first "Unicorn"`
* `python3 slurp.py last "Nature Wallpaper"`

![example][example]

[example]:https://raw.github.com/dfmogk/slurp/master/Example.png "Example"

<h3>Requirements</h3>
The requirements are Python Version 2.*+ (tested for 2.7.1 and 3.3.3 - works.), and the following libraries:

`urllib`,`sys`,`random`,`bs4 (BeautifulSoup)`,`imghdr`,`isdir (os.path)`,`rename (os)`

`bs4` is likely the only one you'll need to install. Do this by executing `$ pip install BeautifulSoup` in your terminal.
