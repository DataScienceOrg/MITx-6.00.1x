# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:59:39 2017

@author: Arnab Ghosh
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadritic = []
myCubic = []
myExponential = []

for i in range (0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadritic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
plt.figure('lin')
plt.clf() # clear the frame
plt.ylim(0,1000)
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot (mySamples, myLinear, 'b-', label="linear", linewidth = 2.0)
plt.legend(loc='upper left')
plt.figure('quad')
plt.clf() # clear the frame
plt.ylim(0,1000)
plt.plot (mySamples, myQuadritic, 'ro', label="quad", linewidth = 3.0)
plt.legend()
plt.figure('cube')
plt.clf() # clear the frame
plt.plot (mySamples, myCubic, 'g^',label="cube", linewidth = 4.0)
plt.figure('expo')
plt.clf() # clear the frame
plt.yscale('log')  # put a function for y axis instead of a regular linear scale
plt.plot (mySamples, myExponential, 'r--', label="exp", linewidth = 5.0)


plt.figure('quad')
plt.xlabel('sample points')
plt.ylabel('quad function')
plt.title("Quadritic")
