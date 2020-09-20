# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 01:28:37 2019
Python (easiest to remember / yet still secure password generator)
@author: Adam ponting's pc

WORK IN PROGRESS

"""

import random

def passwordGenEasy():
    contin = "lesgo"
    password = []
    
    dictlen = 0
    dictionairy = []
    with open('simpleEnglishWordList.txt','r') as open_file:
        for line in open_file:
            if len(list(line)) <= 4:
                dictionairy.append(line)
                dictlen += 1
        
    while contin != "exit" and contin != "":
        contin = input("Welcome to password generator (easy)! type to exit or press enter to continue ")
        if contin == "":
            while len(password) < 4:
                x = random.randint(0,1)
                if x == 0:
                    password.append(dictionairy[random.randint(0,dictlen)])
                elif x == 1:
                    y = random.randint(1,3)
                    nums = "0123456789"
                    password.append("".join(random.sample(nums, y)))
                    
            password = "".join(password)
            
    return password
        
    

if __name__ == "__main__":
    print(passwordGenEasy())