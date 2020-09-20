# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:53:00 2019
Exercise 14 Practice Python: List Remove Duplicates
@author: Adam ponting's pc
"""


def listRemoveDupes(List):
    """
    From Ex10: noDuplicatesv2
    """
    uniqueList = []
    index = 0
    while len(List) > index:
        if List[index] not in uniqueList:
            uniqueList.append(List[index])
        index += 1
    return uniqueList

def setRemoveDupes(List):
    """
    With sets, which are unique themselves (no dupes)
    """
    return list(set(List))

def getList():
    List = []
    while True: #do while loop 
        item = input("Input an item, type finish to finish: ")
        if(item == "finish"): break
        List.append(item)
    return List

def main():
    List = getList()
    print(setRemoveDupes(List))
    print(listRemoveDupes(List))
    
    
main()
    
    
        

