# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:52:56 2017

@author: Arnab Ghosh
"""

def selection_sort(L):
    suffixSt = 0
    steps = 1
    while suffixSt != len(L):
        print("Step# ",steps,L)
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]

        suffixSt += 1
        steps += 1


test = [1, 5, 3, 8, 4, 9, 6, 2]
selection_sort(test)