# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 18:01:40 2017
Write a program to calculate the credit card balance after one year if a 
person only pays the minimum monthly payment required by the credit card 
company each month.
@author: z001hmb
"""

#balance - the outstanding balance on the credit card

#annualInterestRate - annual interest rate as a decimal

#monthlyPaymentRate - minimum monthly payment rate as a decimal

"""
Monthly interest rate= (Annual interest rate) / 12.0

Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)

Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)

Updated balance each month = 
(Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

#annualInterestRate = 0.12
#monthlyPaymentRate = 0.12/12
#balance = 5000

 # Test Case 1:
#balance = 42
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

#Test Case 2:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12
numberOfMonths = 12


minimumMonthlyPayment = 0
monthlyUnpaidBalance = 0



#numberOfMonths = input("Enter number of months :")

for i in range(numberOfMonths):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
 #   print ('Remaining balance: ' + str(round(balance,2)))


print ('Remaining balance: ' + str(round(balance,2)))
    
