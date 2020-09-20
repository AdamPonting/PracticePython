# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 00:30:01 2019
Python Practice Exercise 4
@author: Adam ponting's pc
"""
def numberDivisor(number):
    """
    Takes number as input, creates a list for it's divisors, a list for all 
    numbers between 0 and then appends each value that is a divisor from that
    list to the divisor list (and returns it).
    """
    divisorList = []
    numberList = range(1, int(number/2)+1)
    for element in numberList:
        if number % element == 0:
            divisorList.append(element)
    divisorList.append(number)
    return divisorList
        
#MAIN SEQUENCE    
number = int(input("Please enter a whole number: "))
print(numberDivisor(number))