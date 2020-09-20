# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 15:47:26 2020
Python Practice Exercise 5, 1 Line
@author: Adam ponting's pc
"""
#sorted(ADT) sorts the ADT, into list format
#set(ADT), deletes duplicates by formating the ADT as a set

l1 = [1,1,3,5,7,7,9,11,32,45,56,67]
l2 = [56,70,0,2,5,7,0,32,32,32]
print(sorted(set(l1) & set(l2)))