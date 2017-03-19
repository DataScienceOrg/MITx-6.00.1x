# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:22:27 2017

@author: Arnab Ghosh
"""

def retire(monthly,rate,terms):
    savings=[0]
    base=[0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1+mRate) + monthly]
    return base, savings