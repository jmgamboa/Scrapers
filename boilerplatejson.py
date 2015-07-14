#!/usr/bin/env python
# import re
# import string
import urllib2
import pdb
# The BeautifulSoup module
from bs4 import BeautifulSoup
import html5lib
import json
import datetime
from datetime import date, timedelta

req = urllib2.Request(url) 
con = urllib2.urlopen( req )
data = json.loads(urllib2.urlopen(url).read()) 
url = 'http://esports-cms.thescore.com/api/v1/rivers/top_news/news?limit=30&include_pinned=true&embed_ids=true'
x = TheScore().fetch(url)
