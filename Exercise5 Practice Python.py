# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 00:54:31 2019
Python Practice Exercise 5
@author: Adam ponting's pc
"""
def findCommonElements(list1, list2):
    """
    Takes in two lists, creates a list for common elements, creates an index
    variable, then compares every element in list1 to elements to list2,
    and then deletes every element from list1 in the process to check if that
    element is present elsewhere in list1 (and only appending if it is not).
    """
    commonList = []
    index = 0
    for elementfrom1 in list1:
        if elementfrom1 in list2:
            del list1[index]
            if elementfrom1 not in list1:
                commonList.append(elementfrom1)
        index += 1
    return commonList

def randomList(lengthMax, numberMax):
    """
    Imports random function (inbuilt), exits if maxs are too low, acquires
    random length, creates list to return and then appends elements to that
    list, decreasing length (used like index).
    """
    import random
    if lengthMax == 0 or numberMax == 0:
        print("Choose a higher maximum pls")
        return
    length = random.randint(0, lengthMax)
    thisList = []
    while length >= 0:
        element = random.randint(0, numberMax)
        thisList.append(element)
        length -= 1
    return thisList
        
def findCommonElementsSimple(list1, list2):
    """
    Simplest version to do task 5
    """
    commonList = []
    for elementfrom1 in list1:
        for elementfrom2 in list2:
            if elementfrom1 == elementfrom2 and elementfrom1 not in commonList:
                    commonList.append(elementfrom1)
    return commonList
                    
    
    
#MAIN SEQUENCE
    
#list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lengthMax = int(input("What is the maximum length you require?: "))
numberMax = int(input("What is the maximum number you require?: ")) 
list1 = randomList(lengthMax, numberMax)
list2 = randomList(lengthMax, numberMax)
print(findCommonElements(list1, list2))