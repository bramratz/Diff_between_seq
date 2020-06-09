#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a test file with two strings of equal length, s and t, 
will calculate the hamming distance for s and t. That is it will
find the number of symbols the two sequences differ by. The 
number of differences correpond to the number of point 
mutations that have occured between the two sequences.
 
Created on Mon Jun  8 16:36:22 2020

@author: bram
"""

# Import modules 
import sys

# List to hold to sequences 
seq = []

# Append sequences to list  
with open(sys.argv[1]) as f:
    seq = [line.strip() for line in f] # Strip newline characters

# Initialize counter for the number of differences betwween the two strings 
diffCounter = 0

# Iterate both sequences and compare elements to one another
for val1, val2 in zip(seq[0], seq[1]):
    if val1 == val2:
        continue # If elements are the same do nothing 
    else:
        diffCounter += 1

# Print result to terminal 
print(f'hamming distance between s and t is: {diffCounter}')
