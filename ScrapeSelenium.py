#!/usr/bin/env python
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get("https://www.google.com/flights/#search;f=EWR,JFK,LGA;t=SFO;q=ny+to+san+francisco;d=2015-07-29;r=2015-08-02")
html = driver.page_source
soup = BeautifulSoup(html)
print soup
