#!/usr/bin/env python
import urllib2
import pdb
# The BeautifulSoup module
from bs4 import BeautifulSoup
import html5lib
import json
import argparse

url = 'https://www.distractify.com/excuses-for-your-dog-not-for-humans-1248198479.html'
req = urllib2.Request(url) 
con = urllib2.urlopen( req )
data = json.loads(urllib2.urlopen(url).read()) 
print data