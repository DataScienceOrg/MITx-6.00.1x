# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:23:15 2017

@author: Arnab Ghosh
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    d3={}
    d1b = d1.copy()
    d2b = d2.copy()
    for k1, v1 in d1b.items():
        if k1 in d2b.keys():
            temp_dict ={}
            temp_dict ={k1:f(d1.pop(k1),d2.pop(k1))}
            d3.update(temp_dict) 
#            print("d3 is ",d3)
 
    d1.update(d2) 
    tupret = ()
    tupret = (d3,d1)
    return tupret

def f(v1,v2):
    return v1>v2
    
#d1 = {1:30, 2:20, 3:30, 5:80,6:12} 
#d2 = {1:40, 2:50, 3:60, 4:70,5:80}
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(d1)
print(d2)

dict_interdiff(d1, d2)
