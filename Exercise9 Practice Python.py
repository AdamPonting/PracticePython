# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:37:02 2019
Guessing Game One Exercise 9
@author: Adam ponting's pc
"""
import random

def game():
    """
    My version, relys on no string entry (other than exit) for guess, expects 1
    and 9 to always be boundaries for random int.
    """
    guess = ""
    print("Welcome to the guessing game, where you have to guess what random number has been selected between 1 and 9!")
    while guess != "exit":
        number = random.randint(1, 9)
        guess = input("What is your guess? Type exit to exit, restart to restart and make sure it is an integer: ")
        guesses = 1
        while guess != "restart" and guess != "exit" and guess != str(number):
            if int(guess) > number:
                print("oops too high!")
            elif int(guess) < number:
                print("oops too low!")
            guesses += 1
            guess = input("What is your next guess?: ")
        if(guess != "restart" and guess != "exit"):
            print("Congrats!! You have guessed the correct number: " + str(number) + " with " + str(guesses) + " guess(es)!")
            if(guess != "exit"):
                print("Starting new game...")

        
##MAIN SEQUENCE
game()
    