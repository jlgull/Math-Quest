#!/bin/python3

# Author: Jonathan Heard
# Program to test if the entered number is a power of 2
# Idea came from Tracy Baker.

Guess = int(input("Enter a number to test if it is a power of 2. "))

# Use Boolean a and to test if number is a power of 2.

if (Guess & Guess - 1) == 0:

    print("Entered number ", Guess, " is a power of 2.")

else:

     print("Entered number ", Guess, " is NOT a power of 2.")

