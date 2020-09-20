# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:45:33 2019
Exercise 17 Practice Python: Decode A Web Page
@author: Adam ponting's pc
"""
#for lines 10-12, allows ability to collect page data and seperate parts of it (.text)
import requests

#for lines 17-19, allows ability to search data with specified filters (.title.string)
from bs4 import BeautifulSoup #bs4 is the latest version

url = 'https://www.bbc.co.uk/'
page = requests.get(url)
page_html = page.text

soup = BeautifulSoup(page_html, features = "lxml") 

index = 0
limit = int(input("How many headlines do you wish to show?: "))

pageTitle = soup.title.string
print("Main Title: " + pageTitle)

for pageArticle in soup.find_all(class_="top-story__title"):
    index += 1
    print(str(index) + ". " + pageArticle.text + "\n")
    if index == limit:
        break

"""
Some warning that came up, but had an error message fuck knows what this means.
NOTE: parsing means processing it so the computer understands the data and can
'assign meaning' to it.

UserWarning: No parser was explicitly specified, so I'm using the best available
HTML parser for this system ("lxml"). This usually isn't a problem, but if you 
run this code on another system, or in a different virtual environment, it may
use a different parser and behave differently.

The code that caused this warning is on line 17 of the file
C:/Users/Adam ponting's pc/.spyder-py3/projects/Exercise17 Practice Python.py.
To get rid of this warning, pass the additional argument 'features="lxml"' to
the BeautifulSoup constructor.

Ex. (line 17)
soup = BeautifulSoup(page_html) -> soup = BeautifulSoup(page_html, features = "lxml")
"""