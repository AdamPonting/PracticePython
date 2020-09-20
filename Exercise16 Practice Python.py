# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:07:10 2019
Practice Python Exercise 16: Password Generator
@author: Adam ponting's pc
"""
import random   

def passwordGeneratorShort():
    """
    shorter but provides no user input, no form of validation, no looping of
    generation - and the complexeties that each of these inflict on each other.
    """
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
    length = 8
    print("".join(random.sample(chars, length)))

def passwordGenerator():
    """
    Step by step: The function passwordStrength is called, giving the strength
    of the password and containing that in the variable strength, the same happens
    for the length function and then the (do) while loop initiates, first randomly
    sampling the list of chars with the normal list returned from passwordContent
    and the length from the normal list specified by the length variable. This
    list of elements are then joined and printed. Finally the user is asked if
    they want to generate another, saving the result in contin. Contin is do
    while loop validated. If the answer is y (yes) or n (no), they are further
    asked if they want to use the same strength - and if they do the strength and
    length functions specified earlier are called.
    """
    strength = passwordStrength()
    length = passwordLength(strength)
    
    while True:
        charList = random.sample(passwordContent(strength), length)
        print("".join(charList))
            
        while True:
            contin = input("Do you want to generate another? (y/n): ")
            if(contin == "n" or contin == "y"): break
            else: print("Please input again")
            
        if contin == "n": break
        elif contin == "y":
            newStrength = input("Do you want to use the same strength and length? (y/n): ")
            if newStrength == "n":
                strength = passwordStrength()
                length = passwordLength(strength)      
    
def passwordStrength():
    """
    asks the user for a strength of password choice validating the input with 
    the two lines below it.
    """
    strength = int(input("Enter the password strength: 1 = Strong, 2 = Medium, 3 = Weak: "))
    while strength != 1 and strength != 2 and strength != 3:
        strength = int(input("Sorry didnt get that: 1 = Strong, 2 = Medium, 3 = Weak: "))
    return strength

def passwordLength(strength):
    """
    finds the length of the password to be generated / the number of words in the
    password if strength 3 is chosen
    """
    if strength != 3:
        length = input("Enter the password length, or type r for a random selection between 8 & 16: ")
        if length == "r" or length == "R":
            length = random.randint(8,16)
    else:
        length = random.randint(1,2)
    return int(length)

def passwordContent(strength):
    """
    returns the possible content of the password - medium (2) has letters and
    numbers, strong (1) has that and symbols and weak (3) has a few words from
    a list.
    """
    if strength == 1:
        chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"£$%^&*(){}[]#~:;@<>,.?/\|-_+=') 
    elif strength == 2:
        chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    elif strength == 3: #if taken seriously would use a dictionairy file but do not have the knowledge at the moment
        chars = ['yes','no','somewhere','in','between','is','there','a','point']
    return chars


def main():
    passwordGenerator()
    #passwordGeneratorShort()
    
main()


""" ALTERNATIVE FAIL:
    def passwordGenerator():
    contin = "y"
    strength = passwordStrength()
    if strength != 3:
        length = passwordLength()
    elif strength == 3:
        length = random.randint(1,2)
    
    while contin == "y" or contin == "Y":
        charList = random.sample(passwordContent(strength), length)
        print("".join(charList))
        
        contin = input("Do you want to generate another? (y/n): ")
        if contin == "y" or contin == "Y":
            newStrength = input("Do you want to use the same strength and length? (y/n): ")
            if newStrength != "y" or newStrength != "Y":
                length = passwordLength()
                strength = passwordStrength()
                if strength == 3:
                    length = 1 
    """
