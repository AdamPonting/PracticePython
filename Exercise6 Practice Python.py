# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:37:03 2019
Practice Python Exercise 6
@author: Adam ponting's pc
"""  
def palindrome1(forwards):
    """
    Takes in string input (forwards), creates a list version of that
    (forwardList), reverses the list version through the reverse function, then
    turns that reverse list into a string and prints a yes message if the two
    strings (forwards and backwards) are equal and no if they are not.
    """
    forwardList = list(forwards)
    forwardList.reverse()
    backwards = ''.join(forwardList)
    if forwards == backwards:
        print("Yes it is a palindrome")
    elif forwards != backwards:
        print("No it is not a palindrome")

def palindrome2(forwards):
    """
    Takes in string input (forwards), appends each element in forwards to a
    list version, counting up to it's max length, then utilizing it with range
    to count down to 0 from it, appending to backwardList in reverse order. The
    the positions in the two lists are then compared, outputting the
    corresponding answers .    
    """
    forwardList = []
    backwardList = []
    length = -1
    palindrome = True
    for element in forwards:
        forwardList.append(element)
        length += 1
    for index1 in range(length, 0, -1):
        backwardList.append(forwardList[index1])
    for index2 in range(0, length):
        if forwardList[index2] != backwardList[index2]:
            palindrome = False
    if palindrome == True:
        print("Yes it is a palindrome")
    elif palindrome == False:
        print("No it is not a palindrome")
        
 
def palindrome3(forwards):
    """
    Easy version, reverses string (forwards) with ::-1
    """
    if(forwards == forwards[::-1]):
        print("Yes it is a palindrome")
    else:
        print("No it is not a palindrome")
    

#MAIN SEQUENCE
userInput = input("Enter a string: ")
choice = int(input("Enter a choice: 1, 2 or 3: "))
if choice == 1:
    palindrome1(userInput)
elif choice == 2:
    palindrome2(userInput)
elif choice == 3:
    palindrome3(userInput)
else:
    print("Sorry please choose 1 or 2")
 
        