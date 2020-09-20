# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:59:54 2019
Exercise 2 Practice Python
@author: Adam ponting's pc
"""

#Normal Ex2 + dividing by 4 ext
def OddOrEvenPlus():
    """
    Inputs a variable: number, which is checked on data type and then
    is put into if statements that check if it is even and then a multiple of
    four by utilizing the remainder function: %, printing out the appropiate 
    result.
    """
    number = int(input("Enter number: "))
    if number % 2 == 0:
        print("Number is even: ")
        if number % 4 == 0:
            print("Number is multiple of 4: ")
    elif number % 2 == 1:
        print("Number is odd: ")


#Extension for Ex2        
def DivisorEx():
    """
    inputs 2 variables: num and divNum, which are checked on data type
    and equality to 0. Then prints appropriate message based on if they
    divide evenly/oddly.   
    """
    num = int(input("Enter first number: "))
    divNum = int(input("Enter dividing number: "))
    if num or divNum == 0:
        print("num(" + str(num) + ") divides evenly into divNum(" + str(divNum) + "): ")
        return #breaks/exits function
    if num % divNum == 0:
        print("num(" + str(num) + ") divides evenly into divNum(" + str(divNum) + "): ")
    else:
        print ("num(" + str(num) + ") divides oddly into divNum(" + str(divNum) + "): ")


#Main Sequence
stop = input("Press enter to continue, anything else to stop: ")
if stop == "":
    OddOrEvenPlus()
    stop = input("Press enter to continue, anything else to stop: ")
    if stop == "":
        DivisorEx()
    else:
        exit
else:
    exit