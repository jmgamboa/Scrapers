#!/usr/bin/env python
from StringIO import StringIO
import pycurl
# The BeautifulSoup module
from bs4 import BeautifulSoup
import lxml
import argparse

url = 'http://kotaku.com/'
storage = StringIO()
storage = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEFUNCTION, storage.write)
# again setting headers to prevent bots from scraping
c.setopt(c.HTTPHEADER, ['User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; ',
                                          'header_name2: header_value2'])
c.perform()
c.close()
content = storage.getvalue()
# content lxml
soup = BeautifulSoup(content)

# Beautiful Soup examples
# print soup
spans = soup.find_all('span') # find all spans
# print len(spans)

# find divs with class row
div_rows = soup.find_all('div', {'class' : 'row'})

