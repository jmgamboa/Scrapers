import requests
from bs4 import BeautifulSoup

#get webpage
page = requests.get("https://www.google.com/flights/#search;f=EWR,JFK,LGA;t=SFO;d=2015-07-17;r=2015-07-20")
soup = BeautifulSoup(page.content)

print soup.find('')
