# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 23:27:37 2019
Exercise 19 Practice Python: Decode A Web Page Two 
@author: Adam ponting's pc
"""
import requests

from bs4 import BeautifulSoup

def gatherText():    
    url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
    page = requests.get(url)
    page_html = page.text

    soup = BeautifulSoup(page_html, features="lxml")
    """
    Whole task is fucked caus url now longer is in the right format - NO OBJECTS
    SHARE A DIV / not all text is in para (p) format + its impossible to collect the
    data without selecting every individual classed block by itself (completely
    inefficient and cannot be applied to other websites easily)
    
    All in all its so fucking fucked and most likely on purpose by vanity fair.
    """

if __name__ == "__main__": #Main method
    gatherText()

