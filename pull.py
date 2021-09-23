import csv
import requests
from bs4 import BeautifulSoup
import re

response = requests.get('https://naruto.fandom.com/wiki/Music')
soup=BeautifulSoup(response.text,"html.parser")
x=soup.find("div", class_="organizationName")

print(x)
#print(soup)
#for tag in x:
#    print(tag.text)
