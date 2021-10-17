#!/bin/python3
#
# Filename: yx-jlh1.py
# Built from Python program yx.py by Tracy Baker
# Author: Jonathan Heard
# Purpose: Review the Collatz (3X+1) math challenge.

# Tracy couldn't just leave well enough alone... Learning some Python tonight

""" Set initial variables
    i = the iteration counter
    index = the location within the MasterList of the start of
        the LoopList.
    Creating Odd and Even to keeping track of
    the count of Odd and Even results. """
i = Odd = Even = 0

# End of Variables

# Get the starting number
Seed = int(input("\n\nEnter the starting value: "))

# Get the multiplier
Multiplier = int(input("\n\nEnter a multiplier, Odd not Even. For example 3, 5, 7, etc..: "))

""" Set working value of Num to value entered in Seed.
    Set Max to Seed value, in the case the Seed value is the maximum value """

Num = Max = Seed

# Create and initialize the MasterList and LoopList lists
MasterList = []
LoopList = []

# Create an infinite loop. The loop will be broken upon a detected loop.
while True:

    # Check to see that Num is not already in the MasterList array
    # then add it and proceed with the while loop.
    if Num not in MasterList:

        # Add Num to MasterList
        MasterList.append(int(Num))

        print("Iteration #", i, ": Num =", int(Num))

        i += 1

        # If Num is even, divide by 2
        if Num % 2 == 0:
            Even += 1
            Num = Num / 2

        # If Num is odd then apply yx+1 formula, with
        # y being Num and x being the Multiplier entered.
        else:
            Odd += 1
            Num = Num * Multiplier + 1

        # Keep track of the greatest number found
        if Num > Max:
            Max = Num

    # If Num is in MasterList, use list comprehension to make the LoopList.
    else:
        #for Index in range(MasterList.index(Num), len(MasterList)):
        #    LoopList.append(MasterList[Index])
        LoopList = [MasterList[Index] for Index in range(MasterList.index(Num) , len(MasterList))]
        break

""" ##### END OF while LOOP ##### 
    Print out all the findings. """

print("\nUsing the formula (", int(Multiplier), "* x ) + 1")

print("\nLoop Found!", LoopList)

print("\nInitial Number =", Seed)

print("\nLargest Number =", int(Max))

print("\nTotal iterations = ", i)

print("\nThere were", Even, "even numbers and", Odd, "odd numbers.")
print("\nSpeaking in Percentages, there were ")
print("\t{:.2%}".format(Even / i), "even numbers and")
print("\t{:.2%}".format(Odd / i), "odd numbers.")

""" End of Program """