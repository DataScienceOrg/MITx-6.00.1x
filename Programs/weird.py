# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 18:14:08 2017

@author: z001hmb
"""

if __name__ == '__main__':
    n = int(input())
    
# If  is odd, print Weird
    if n%2 != 0:
        print ("Weird")
    else:
        if n >= 2 and n <=5: # If  is even and in the inclusive range of 2 to 5 , print Not Weird 
            print("Not Weird")
        elif n >= 6 and n <=20: # If  is even and in the inclusive range of 6 to 20 , print Weird
            print("Weird")            
        elif n > 20: # If  is even and greater than 20, print Not Weird
            print("Not Weird")

 