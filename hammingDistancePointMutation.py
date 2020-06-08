#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two strings of equal length, s and t, will calculate the 
hamming distance for s and t. That is it will find the number
of symbols the two sequences differ by. The number of differences 
correpond to the number of point mutations that have occured
between the two sequences.
 
Created on Mon Jun  8 16:36:22 2020

@author: bram
"""

# Import modules 
import sys

# Save strings to be compared as variables 
s = list(sys.argv[1])
t = list(sys.argv[2])

# Initialize counter for the number of differences betwween the two strings 
diffCounter = 0

# Iterate both lists and compare elements to one another
for val1, val2 in zip(s, t):
    if val1 == val2:
        continue # If elements are the same do nothing 
    else:
        diffCounter += 1

# Print result to terminal 
print(f'hamming distance between s and t is: {diffCounter}')
