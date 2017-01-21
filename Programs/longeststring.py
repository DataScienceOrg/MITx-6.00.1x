# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 08:35:23 2017


Problem 3
15/15 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in 
alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

@author: z001hmb
"""
s = 'azcbobobegghakl'
longstr1 = s[0]
longstr2 = ''
for i in range(1,(len(s)),1):
    if s[i] >= s[i-1]:
        longstr1 = longstr1 + s[i]
        #print("Longstr1 value: " + longstr1)
    else:
        if len(longstr1) > len(longstr2):
            longstr2 = longstr1
            #print("Longstr2 value: " + longstr2)
        longstr1 = s[i]

if len(longstr1) > len(longstr2):
    print("Longest substring in alphabetical order is: ", longstr1)
else:
    print("Longest substring in alphabetical order is: ", longstr2)

