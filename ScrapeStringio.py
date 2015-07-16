#!/usr/bin/env python
from StringIO import StringIO
import pycurl
# The BeautifulSoup module
from bs4 import BeautifulSoup
import lxml
import argparse

url = 'https://www.distractify.com/excuses-for-your-dog-not-for-humans-1248198479.html'
storage = StringIO()
storage = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEFUNCTION, storage.write)
c.setopt(c.HTTPHEADER, ['User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; ',
                                          'header_name2: header_value2'])
c.perform()
c.close()
content = storage.getvalue()
soup = BeautifulSoup(content, "lxml")
print soup
