# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:53:14 2019
Exercise on list Comprehension
@author: Adam ponting's pc
"""
def listEven1(list):
    """
    one line
    """
    return [element for element in list if element % 2 == 0]
    
def listEven2(list):
    """
    not one line but with base logic
    """
    evenList = []
    for element in list:
        if element % 2 == 0:
            evenList.append(element)
    return evenList


## MAIN SEQUENCE 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

choice = int(input("Type 1 for one line code, 2 for two+ line code. "))
while choice != 1 and choice != 2:
    choice = int(input("Try again: 1 for one line code, 2 for two+ lines of code. "))   
if choice == 1:
    print(listEven1(a))
elif choice == 2:
    print(listEven2(a))
    
    