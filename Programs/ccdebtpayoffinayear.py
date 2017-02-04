# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 18:55:26 2017

@author: Arnab Ghosh
"""



balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12

#print("Monthly Int rate: ",str(round(monthlyInterestRate,2)))

def calcpremium(balance,monthlyInterestRate,premium):
    for i in range(12):
        balance = (balance - premium)* (1+monthlyInterestRate)
        #print("Balance after month: ",str(i), ":",str(round(balance,2)))
    return balance



premium = 10
remainingAmount = 0

while remainingAmount >= 0:    
    premium += 10 # since the premium has to be multiple of 10
    #print("Running with premium: ",str(round(premium,2)))

    remainingAmount = calcpremium(balance,monthlyInterestRate,premium)


print("Lowest Payment:",str(round(premium)))

