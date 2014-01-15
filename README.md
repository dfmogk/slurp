slurp.py
========

Gets a random image from deviantart, based on a search string.
--------------------------------------------------------------

Usage: `$ python slurp.py [random/first/last] "Search String" "savedir"`
(Note: `savedir` is optional)

* `random` gets a random image from the first search page.
* `first` gets the first image from the search page.
* `last` gets the last image from the search page.

slurp.py prints the link to the raw image, and, if `savedir` is set, saves the image there.
