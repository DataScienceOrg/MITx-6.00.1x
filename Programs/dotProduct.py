# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 07:16:52 2017

@author: Arnab Ghosh
"""


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    For example, if listA = [1, 2, 3] and listB = [4, 5, 6], 
    the dot product is 1*4 + 2*5 + 3*6, meaning your function 
    should return: 32
    '''
    # Your code here
    product = 0
    for i in range(len(listA)):
        product = product + listA[i]*listB[i]
    return product
        
#listA = [1, 2, 3]
#listB = [4, 5, 6]
#x=dotProduct(listA, listB) # returns 32