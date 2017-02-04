# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 18:55:26 2017

@author: Arnab Ghosh
"""

#Test Case 1:
balance = 320000
annualInterestRate = 0.2

#Test Case 2:
#balance = 999999
#annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12

def calcpremium(balance,monthlyInterestRate,premium):
    for i in range(12):
        balance = (balance - premium) * (1+monthlyInterestRate)
    return balance



remainingAmount = balance
high = (balance * ((1+monthlyInterestRate)**12))/12
low = balance/12
premium = low

while round(remainingAmount,2) !=0:
    if remainingAmount > 0:   
        low = premium
        premium = (high+low)/2
        remainingAmount = calcpremium(balance,monthlyInterestRate,premium)
    elif remainingAmount < 0:
        high = premium
        premium = (high+low)/2
        remainingAmount = calcpremium(balance,monthlyInterestRate,premium)
        

print("Lowest Payment:",str(round(premium,2)))