#!/bin/python3
#
# Filename: 3x_1V1
# Built from Bash Script 3xtb1.sh and 3xtb2.sh (developed by Tracy Baker)
# Author: Jonathan Heard
# Purpose: Review the Collatz (3X+1) math challenge.
#
# Set initial variables
# i is the iteration counter

i = 0

# Creating Odd and Even to keeping track of
# the count of Odd and Even results.

Odd = 0; Even = 0

# End of Variables

# Get the starting number

Seed = int(input("Enter the starting value: "))

# Set working value of Num to value entered in Seed.

Num = Seed

# Set Max to Seed value, in the case the Seed value is the maximum value

Max = Seed

while Num != 1 and Num > 0:

    i += 1

    if Num % 2 == 0:
        Even += 1
        Num = int(Num) / 2
    else:
        Odd += 1
        Num = int(Num) * 3 + 1

        # i += 1

        if Num > Max:
            Max = Num

    print("Iteration # ",  i,  " : Num = ",  int(Num))


print("\nInitial Number = ", Seed)

print("\nLargest Number = ", int(Max))

print("\nTotal iterations = ", i)

print("\nThere were ", Even, " Even numbers and ", Odd, " Odd numbers.")
print("Speaking in Percentages, there were ")
print("\t", (Even / i)*100, "% Even numbers and")
print("\t", (Odd / i)*100, "% Odd numbers.")