# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:21:21 2019

@author: Asus
"""
from random import shuffle
enlistsize = int(input("Enter List Size :"))
enlist = list()
for i in range(enlistsize):
    enlist.append( input("Enter the Item :"))
print("Original:",enlist)
def listry(enlist):
    shuffle(enlist)
    print("Shuffled :",enlist)
listry(enlist)