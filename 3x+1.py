#!/bin/python3
#
# Filename: 3X+1.sh
# Author: Jonathan Heard
# Purpose: Review the Collatz (3X+1) math challenge.
#
# Set initial variables
# i is the iteration counter

i = 0

# Max is the maximum value seen in Num

Max = 0

# End of Variables

# Get the starting number

Seed = int(input("Enter the starting value: "))

# Set working value of Num to value entered in Seed.

Num = Seed

print("\nInitial Number = ", Seed, "\n")

while Num != 1:

    i += 1

    if Num % 2 == 0:
#       print("\nEven")
        Num = int(Num) / 2
#       print(Num)
    else:
#       print("\nOdd")
        Num = int(Num) * 3 + 1
#       print(Num)

        # i += 1

        if Num > Max:
            Max = Num

    print("Iteration # ",  i,  " : Num = ",  int(Num))


print("\nInitial Number = ", Seed)

print("\nLargest Number = ", int(Max))

print("\nTotal iterations = ", i)
