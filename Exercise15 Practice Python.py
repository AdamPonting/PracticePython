# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 01:05:07 2019
Exercise 15 Practice Python: Reverse Word Order
@author: Adam ponting's pc
"""
def reverseStringV1(string):
    """
    creates a list for the reverse string, splits the passed in string
    (just by " "), sets index as the length - 1 (position in the list
    from the last item), then appends the list of words backwards to reverseList
    using index. Finally the list of words in reverseList is joined with .join
    and contained in finalString - which is then returned.
    """
    reverseList = []
    splitString = string.split()
    index = len(splitString) - 1
    while index >= 0:
        reverseList.append(splitString[index])
        index -= 1
    finalString = " ".join(reverseList)
    return finalString

def reverseStringVShort(string):
    """
    ridiculous, not sure how it does it exactly but hey ho
    """
    return ' '.join(string.split()[::-1])

def reverseStringV2(string):
    """
    The best method / most reasonable, .insert(index, obj) inserts obj at index
    """
    splitString = string.split()
    finalString = []
    for word in splitString:
        finalString.insert(0, word)
    return " ".join(finalString)
    

def main():
    string = input("gimme a string: ")
    #print(reverseStringV1(string))
    #print(reverseStringVShort(string))
    print(reverseStringV2(string))
    
main()
        
