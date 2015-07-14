#!/usr/bin/env python
# import re
# import string
# import urllib2
import pdb
# The BeautifulSoup module
from bs4 import BeautifulSoup
import MySQLdb
import html5lib
import urllib2
import datetime
from datetime import date, timedelta

# db = MySQLdb.connect(
#                host='45.33.70.49',
#                user='marko',
#                passwd='dEg-fiF-jit-pid-yec-wI-Aj-',
#                db='datnexusdb')


class TheScoreEsports:

	articles = []

	def fetch(self, url):
		req = urllib2.Request(url)
		con = urllib2.urlopen( req )
		soup = con.read()
		soup = BeautifulSoup(soup, "html5lib")
		print soup

url = 'http://www.golfdigest.com/'
x = TheScoreEsports().fetch(url)
