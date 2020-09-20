# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 01:24:14 2019
Python Practice Exercise 3
@author: Adam ponting's pc
"""
def acquireList():
    """
    Acquiring list by length input and then while loop oriented appending of
    individual numbers.
    """
    length = int(input("What is the length of the list you would like?: "))
    index = 0
    a = []
    while index < length:
        a.append(int(input("What is the number you would like at position " + str(index) + "?: ")))
        index += 1
    return a

def printListFivePlus(a):
    #Input for what extension task
    method = int(input("For line by line method type 1, for list method type 2, for extra 3 type 3: "))
    # declaring b for task 1/2/3
    b = []
    if method == 3:
        number = int(input("Gimme a less than num: "))
    #checking method is within bounds
    if method < 1 or method > 3: #exit if other number
        print("Sorry didnt quite get that, exiting")
        return
    #for every element in their list, with ifs for each method
    for element in a:
        if method == 1:
            if element < 5:     #Line by line printout
                print(str(element) + " is less than 5. \n")
        if method == 2:
            if element < 5:     #List printout
                b.append(element)
        if method == 3:         #List printout w/ user input for less than
            if element < number:
                b.append(element)
    print(b)
    
## MAIN SEQUENCE
printListFivePlus(acquireList())