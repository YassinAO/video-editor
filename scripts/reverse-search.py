import urllib 
from urllib.request import urlopen
from http.cookiejar import CookieJar
import re

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

def imageLookup():

    imagepath  = 'https://www.voorbrood.nl/site/2-zits-bank-valerio-valerio-2/$FILE/EasySofa-Valerio-2-zits-01-450x300.jpg'
    googlepath = 'https://www.google.com/imghp?image_url='+imagepath
    sourceCode = opener.open(googlepath).read()

    findlinks = re.findall(b'https://www.google.com/imghp%3Fq%3D(.*?)"',sourceCode)
    for findLink in findlinks:
        print(findLink)

imageLookup()