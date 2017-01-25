# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 19:09:23 2017

@author: Arnab Ghosh
"""

print("Please think of a number between 0 and 100!")
high = 100
low = 0
guess = 0
choice = ''

while choice!='c':
    guess = int((low+high)/2)
    print("Is your secret number " + str(guess) + "?")
    choice = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if choice == 'h':
        high = guess
    elif choice == 'l':
        low = guess
    elif choice == 'c':
        print("Game over. Your secret number was: " + str(guess))
    else:
        print("Sorry, I did not understand your input.")

