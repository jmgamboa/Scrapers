#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import argparse
# requests is the popular HTTP request module
page = requests.get("http://vice.com/")
soup = BeautifulSoup(page.content)

# example for getting all link hrefs
links = soup.find_all('a')
for link in links:
	print 'this is an href', link['href']