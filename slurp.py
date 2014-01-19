'''
        Script: slurp.py
 Creation Date: 14th of January, 2014
Finishing Date: 14th of January, 2014
       License: GPL3 (the script)
       Made by: dfmogk (digitalforest.dyndns.org), samhain13 (abcruz.com)
   Description: Just getting pictures from deviantart.
                Get an image for any search string.
                Random, first, or last supported. =)


'''

import sys


# For Python2/Python3 compatibility

try:
    from urllib.request import urlopen, urlretrieve
    # Python 3+, urlopen and urlretreive were moved to urllib.request
except ImportError:
    try:
    	# Python 2.*
        from urllib import urlopen, urlretrieve
    except:
        print("Cannot import urlopen and urlretrieve.")
        sys.exit()
except:
    print("Cannot import urlopen and urlretrieve.")
    sys.exit()

import random                 # for "random" mode
import imghdr                 # to get the image suffix through MIME-type
from bs4 import BeautifulSoup # to XS the DOM
from os.path import isdir     # to check the target directory if downloading 
from os import rename         # to add the suffix.

''' Checking arguments. No defaults for now. '''

if len(sys.argv) is not 3 and len(sys.argv) is not 4:
	print("Argument count mismatch.")
	print("Usage: " + sys.argv[0] + " [first | last | random] <search string>")
	sys.exit()

pagecontent = urlopen("http://www.deviantart.com/?q=" + sys.argv[2].replace(" ","+").replace(",","+")).read()

''' Checking if HTML is fully loaded '''

if "</html>" not in str(pagecontent[-10:]):
	print("Searchpage HTML failed. Dropping out...")
	sys.exit()

pagedom = BeautifulSoup(pagecontent)

''' Checking if DOM is okay '''

if pagedom is None:
	print("Searchpage DOM tree broken. Dropping out...")
	sys.exit()

''' Checking if any image tile is present (should've got class="t" ) '''
if pagedom.find_all("a", {"class":"t"}) is None:
	print("Searchpage Element not found. Dropping out...")
	sys.exit()

elements = pagedom.find_all("a", {"class":"t"})
# t = title (is a)

images = []

for tmpObject in elements:
	''' Going through every element present which is an image tile. '''
	if tmpObject is not None:
		images.append(tmpObject.get("href"))

''' Checking which element we should send out. '''

imagelink = ""

if "random" in sys.argv[1]:
	imagenumber = random.randint(0,len(images) - 1) # <-- Pick a random element
elif "first" in sys.argv[1]:
	imagenumber = 0             # <-- Pick the first element
elif "last" in sys.argv[1]:
	imagenumber = len(images)-1 # <-- Pick the last element

imagelink = images[imagenumber]

''' Now, switching to the image page so we get the high-res picture '''

imgpagecontent = urlopen(imagelink).read()

if "</html>" not in str(imgpagecontent[-10:]):
	print("Image Page HTML failed. Dropping out...")
	sys.exit()
imgpagedom = BeautifulSoup(imgpagecontent)

if imgpagedom is None:
	print("Image Page DOM tree broken. Dropping out...")
	sys.exit()

if imgpagedom.find("img",{"class":"dev-content-normal"}) is None:
	print("Image Page Element not found. Dropping out...")
	sys.exit()

# print description and link

print(str(imgpagedom.find_all("title"))[8:][:-23] + ", " + images[imagenumber])

if len(sys.argv) is 4:
    if not isdir(str(sys.argv[3])):
        print(str(sys.argv[3]) + " doesn't exist. :(")
    pathname = str(sys.argv[3]) + "/" + (str(images[imagenumber]).rsplit("/",1)[1])
    urlretrieve(imgpagedom.find("img",{"class":"dev-content-normal"}).get("src"),pathname)
    rename(pathname,pathname + "." + imghdr.what(pathname))
