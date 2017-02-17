# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:03:13 2017

@author: Arnab Ghosh
"""

while True:
    try:
        n = input ("Please give a integer...")
        n = int(n)
        break
    except ValueError:
        print("Input not integer, try again...")
print("Correct Input of an integer")