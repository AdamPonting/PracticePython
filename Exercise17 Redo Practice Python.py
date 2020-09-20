# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:32:59 2020
Exercise 17 Practice Python: Decode A Web Page (Redo)
@author: Adam ponting's pc
"""
import requests
from bs4 import BeautifulSoup

websiteHtml = (requests.get("https://www.nytimes.com/")).text
siteSoup = BeautifulSoup(websiteHtml, 'html.parser')

index = 0
for titles in siteSoup.find_all(class_="balancedHeadline"):
    print("mother fucker")
    if index > 5: break
    print(titles.text)
    index += 1
    

