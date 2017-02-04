# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 18:31:28 2017

@author: Arnab Ghosh
"""

import math

def polysum(n,s):
    """
    n:int
    s:int or float
    
    return:float
    """
    pArea = (0.25 * n * s * s)/math.tan(math.pi/n)
    pPerimSq = (n * s) * (n * s)
    pTotal = pArea + pPerimSq
    return round(pTotal,4)