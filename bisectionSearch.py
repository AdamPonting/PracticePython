# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
maximum = 0
minimum = 1
while maximum < minimum:
    maximum = float(input("Enter max "))
    minimum = float(input("Enter low "))

number = maximum+1
while number > maximum or number < minimum:
    number = float(input("Enter number between max and low "))

guess = ((maximum+minimum)/2.0) 
number_guesses = 0

while(guess != number):
    if guess > number:
        maximum = guess
    elif guess < number:
        minimum = guess
    guess = ((maximum+minimum)/2.0)    
    number_guesses += 1
    print("current guess =", guess)
print('number of guesses =', number_guesses)
print(guess, "is the number!")
