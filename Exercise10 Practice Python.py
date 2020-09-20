# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:15:59 2019
List Overlap Comprehensions
@author: Adam ponting's pc
"""
def findCommonElements(list1, list2):
    commonList = [element1 for element1 in list1 for element2 in list2 if element1 == element2]
    return noDuplicatesv2(commonList) #alternatively could do set(commonlist)

def noDuplicates(List):
    """
    works, sorts inputted list (only numbers) then deletes any duplicates that
    come before the said index position in List in the while loop
    """
    index = 0
    List.sort()
    while index != len(List) - 1:
        if index > 0:
            if List[index] == List[index - 1]:
                del List[index]
        index += 1
    return List
 
def noDuplicatesv2(List):
    """
    D's solution - takes an empty list and appends if the current element is not in it.
    """
    uniqueList = []
    index = 0
    while len(List) > index:
        if List[index] not in uniqueList:
            uniqueList.append(List[index])
        index += 1
    return uniqueList
          

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(findCommonElements(a,b))