# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:52:54 2019
Practice Python Exercise 20: Element / Binary Search
@author: Adam ponting's pc
"""
def elementSearch(numbers):
    number = int(input("Enter a number which could be in the list: "))
    
    lIndex = 0 #low index
    mid = int(((len(numbers) - 1) / 2))
    if len(numbers) > 1:
        hIndex = (len(numbers) - 1 ) #high index
    else:
        hIndex = 1
    result = False
    
    while numbers[mid] != number:
        if numbers[mid] > number:
            hIndex = mid - 1
        elif numbers[mid] < number:
            lIndex = mid + 1
        else:
            result = True
        mid = lIndex + (hIndex - lIndex) / 2



    if result == True:
        print("It is in the list")
    elif result == False:
        print("It is NOT in the list")
        


if __name__ == "__main__":
    numbers = [2, 4, 6, 8, 10]
    elementSearch(numbers)
    
