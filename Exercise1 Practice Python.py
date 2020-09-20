# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Tue Jun 11 17:30:03 2019
Exercise 1 Python practice
@author: Adam ponting's pc
"""

def solution(name, age):
    """
    function that takes in name, age and prints their age at 100
    (if the current year is 2020)
    """
    year = 2020 - age + 100
    print("Hi", name, "it will be", year, "when you turn 100")

#Acquiring name and age
name = input("Whats your name?: ")
age = int(input("Whats your age? - give as integer: "))

#Acquiring year turning 100 and printing
solution(name, age)