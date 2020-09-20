# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:27:59 2019
Python Practice Exercise 11: Check Primality Functions
@author: Adam ponting's pc
"""

def isPrimev1(number):
    """
    Version 1 using list comprehensions
    """
    numberList = range(2, int(number/2)-1)
    divisors = [element for element in numberList if number % element == 0]
    prime = False
    if(len(divisors) == 0): prime = True
    return prime

def isPrimev2(number):
    """
    Version 2 using while loops, believe this one to be more efficient
    """
    numberList = range(2, int(number/2)-1)
    index = 0
    prime = True
    while index < len(numberList) and prime == True:
        if(number % numberList[index] == 0):
            prime = False
        index += 1
    return prime
        

number = int(input("Give me a number to find prime of: "))
print("Prime is", isPrimev2(number))