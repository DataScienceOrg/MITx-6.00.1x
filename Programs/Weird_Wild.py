# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:44:50 2017

@author: Arnab Ghosh
"""

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y
        
        
x = 7
y = 8

w1 = Weird(10, 12)
print(w1.getX())