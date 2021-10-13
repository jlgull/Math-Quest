#!/bin/python3
#
# Filename: yx-jlh1.py
# Built from Python program yx.py by Tracy Baker
# Author: Jonathan Heard
# Purpose: Review the Collatz (3X+1) math challenge.

# Tracy couldn't just leave well enough alone... Learning some Python tonight

""" Set initial variables
    i is the iteration counter
    index is the location within the MasterList of the start of
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

""" Note: the numpy module / package may need to be installed for array support
    In RHEL/CentOS, it is: python3-numpy.x86_64 """

# Create and initialize the MasterList and LoopList arrays
MasterList = []
LoopList = []

# Create an infinite loop. The loop will be broken upon a negative number
# or detected loop.
while True:

# Check to see if Num is already in the MasterList array
    if Num not in MasterList:

        # Add Num to MasterList
        MasterList.append(int(Num))

        """" # If Num is already in LoopList, the loop is found
        # break the while loop
        # if Num in LoopList:
        #     break

        # Otherwise, add Num to LoopList
        else:
            LoopList.append(int(Num))

    # Add Num to MasterList
    MasterList.append(int(Num)) 
   # New method of finding the LoopList by jlh
    try:
        MasterListIndex = MasterList.index(Num)
        for LoopListIndex in range(MasterListIndex, len(MasterList)):
            LoopList.append(MasterList(LoopListIndex))
            break

    except ValueError:
        MasterList.append(int(Num)) """

    i += 1

    # If Num is even, divide by 2
    if Num % 2 == 0:
        Even += 1
        Num = Num / 2

    # If Num is odd then apply yx+1 formula it
    else:
        Odd += 1
        Num = Num * Multiplier + 1

    # Keep track of the greatest number found
    if Num > Max:
        Max = Num

    print("Iteration #",  i, ": Num =",  int(Num))

    # If Num reaches 1, the loop has been found, break out of the loop
    # if Num == 1:
    if Num in MasterList:
       # MasterList.append(int(Num))
        Index = MasterList.index(Num)
        for LoopListIndex in range(Index, len(MasterList)):
            LoopList.append(MasterList[LoopListIndex])
        break

""" ##### END OF while LOOP ##### """

print("\nUsing the formula (", int(Multiplier), "* x) + 1")

print("\nLoop Found!", LoopList)

print("\nInitial Number =", Seed)

print("\nLargest Number =", int(Max))

print("\nTotal iterations = ", i)

print("\nThere were", Even, "even numbers and", Odd, "odd numbers.")
print("Speaking in Percentages, there were ")
print("\t", (Even / i)*100, "% even numbers and")
print("\t", (Odd / i)*100, "% odd numbers.")

""" End of Program """
