# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:23:33 2019
Exercise 18 Practice Python: Cows and Bulls Game
@author: Adam ponting's pc
"""
import random

def bullsancows():
    guess = 0
    index = 1 #is used for while loops 
    digitList = [] #contains all the digits in the number to guess
    
    #to generate the number to guess with a while loop validation
    while index <= 4:
        digit = random.randint(0,9)
        while index == 1 and digit == 0: #to make sure it is a 4 digit number (not 0001)
            digit = random.randint(0,9)
        digitList.append(str(digit))
        index += 1

    totalCows = 0 #measures the total correct guesses
    totalBulls = 0 #measures the total incorrect guesses
    
    print("Welcome to Cows and Bulls! you must guess a randomly generated 4 digit number" + "\n" + "The tally of correct guesses made are represented by cows, and incorrect guesses by bulls.")
    
    #to ask input of a guess and then compares individual digits of the guess and actual number
    while guess != int("".join(digitList)):
        guess = 0
        while guess < 1000 or guess > 9999:
            guess = int(input("Please enter your guess (4 digits), type exit to exit: "))
        digits = list(str(guess))
        index = 0
        cows = 0 #measures the correct guesses
        bulls = 0 #measures the incorrect guesses
        while index < 4:
            if digits[index] == digitList[index]:
                cows += 1
                totalCows += 1
            elif digits[index] != digitList[index]:
                bulls += 1
                totalBulls += 1
            index += 1
        print("Your score is:", cows,"cows and", bulls, "bulls.")
                
    print("Congratulations you have guessed correctly!!, with", totalCows, "cows and", totalBulls, "bulls in total.")
    
                
            
    
        
    
def main():
    bullsancows()

main()
