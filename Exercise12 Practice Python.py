# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:48:48 2019
Practice Python Ex 12: List Ends
@author: Adam ponting's pc
"""
def getListEnds(List):
    if(len(List) < 2): return "enter a list with 2+ values"
    endList = []
    endList.append(List[0])
    endList.append(List[len(List) - 1])
    return endList

def getList():
    List = []
    while True: #do while loop 
        item = input("Input an item, type finish to finish: ")
        if(item == "finish"): break
        List.append(item)
    return List

List = getList()
print(getListEnds(List))
        
