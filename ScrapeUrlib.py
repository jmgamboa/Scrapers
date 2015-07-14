#!/usr/bin/env python
from bs4 import BeautifulSoup
import html5lib
import urllib2

url = 'https://www.distractify.com/excuses-for-your-dog-not-for-humans-1248198479.html'
req = urllib2.Request(url)
con = urllib2.urlopen( req )
soup = con.read()
soup = BeautifulSoup(soup, "html5lib")
print soup

