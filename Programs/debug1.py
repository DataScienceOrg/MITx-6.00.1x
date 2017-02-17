# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:10:55 2017

@author: z001hmb
"""

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        #print ("i am herein elif with x=",x,"and a=",a)
        return x
    else:
        #print ("i am here in else with x=",x,"and a=",a)
        return(rem(x-a, a))
        
        
        
        
#rem(7, 5)
rem(2, 5)