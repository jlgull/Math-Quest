#!/bin/python3
#
# Filename: 3x_1V1
# Built from Bash Script 3xtb1.sh and 3xtb2.sh (developed by Tracy Baker)
# Author: Jonathan Heard
# Purpose: Review the Collatz (3X+1) math challenge.

# Tracy couldn't just leave well enough alone... Learning some Python tonight

#
# Set initial variables
# i is the iteration counter
# Creating Odd and Even to keeping track of
# the count of Odd and Even results.
i = Odd = Even = 0

# End of Variables

# Get the starting number
Seed = int(input("\n\nEnter the starting Seed (enter 0 for a random number): "))

#### If 0 is chosen at the previous input, then a random number is to be chosen
# the random module needs to be imported
# random.shuffle() will shuffle the items in a list (RandomList) - this is used to randomize the
#                  the number that will be multipled with the number generated with random.random(),
#                  by selecting the number that ends up in index 0 (RandomList[0])
# random.random() function will return a random non-integer number between 0 and 1 - to 17 decimal places
if Seed == 0:
    import random
    RandomList = [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
    random.shuffle(RandomList)
    Seed = int(random.random()*RandomList[0])
    print ("\nRandom Seed is",Seed)

# Get the multiplier
Multiplier = int(input("\nEnter a multiplier. For example 3, 5, 7, etc..: "))

# Set working value of Num to value entered in Seed.
# Set Max to Seed value, in the case the Seed value is the maximum value
Num = Max = Seed

### Note: the numpy module / package may need to be installed for array support
### In RHEL/CentOS, it is: python3-numpy.x86_64
# Create and initialize the MasterList and LoopList arrays
MasterList=[]
LoopList=[]

# Create an infinite loop. The loop will be broken upon a negative number
# or detected loop.
while True:

    # Check to see if Num is already in the MasterList array
    if Num in MasterList:

        # If Num is already in LoopList, the loop is found
        # break the while loop
        if Num in LoopList:
            print ("\nLoop Found!",LoopList)
            break

        # Otherwise, add Num to LoopList
        else:
            LoopList.append(int(Num))

    # Add Num to MasterList
    MasterList.append(int(Num))

    i += 1

    # If Num is even, divide by 2
    if Num % 2 == 0:
        Even += 1
        Num = Num / 2

    # If Num is odd then apply yx+1 formula it
    else:
        Odd += 1
        Num = Num * Multiplier + 1

    # If Num has gone negative, break out of the loop
    if Num < 1:
        break

    # Keep track of the greatest number found
    if Num > Max:
        Max = Num

    print("Iteration #",  i, ": Num =",  int(Num))

##### END OF while LOOP #####

print ("\nUsing the formula",Multiplier,"x+1")

print("\nInitial Number =", Seed)

print("\nLargest Number =", int(Max))

print("\nThere were", Even ,"even numbers and", Odd, "odd numbers.")
print("Speaking in Percentages, there were \n\t", (Even / i)*100,"% even numbers and")
print("\t", (Odd / i)*100,"% odd numbers.")

print("\nTotal iterations = ", i)