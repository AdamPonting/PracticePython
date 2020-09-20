# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:25:55 2019
Practice Python Ex 13: Fibonacci
@author: Adam ponting's pc
"""
def Fibonacci():
    length = int(input("How many Fibonacci numbers would you like?: "))
    index = 1
    if length == 1:
        numbers = [1]
    elif length > 0:
        numbers = [1,1]
        while length-1 > index:
            numbers.append(numbers[index] + numbers[index-1])
            index += 1
    return numbers

print(Fibonacci())
        
