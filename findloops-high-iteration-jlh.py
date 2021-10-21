#!/bin/python3

"""
Original findloop.py written by Tracy Baker

Intent of high iteration rewrite is to collect starting seed with
iteration counts greater than assigned value
Looplist generated using concepts from Jonathan Heard,
which only processes numbers if they aren't in the master number
list. Once a number is repeated, the loop number list can be
constructed.

# Section to import all modules used in this program

# Eventually, this will write to a file. So, sys is needed
# also, "copy" stdout to original_stdout. This will allow
# redirection of stdout to a file using print()
# os needs to be imported to delete the log file, if it exists.
# Otherwise, it just continues to grow with each execution of the script
# If time is being measured the time module will be needed. """

import sys

import os

import time

# End of import section

original_stdout = sys.stdout

# Set the log file name
LogFile = "findloops.py.log"
LargeFile = "Large-Interval.py.log"

if os.path.exists(LogFile):
    os.remove(LogFile)

if os.path.exists(LargeFile):
    os.remove(LargeFile)

os.system('clear')

print("\nThe log file being used is:", LogFile)

# MaxSize = sys.maxsize  # Used to set the largest number to test.

MaxSize = int(input("Enter the largest number to be tested: "))

print("\nThe numbers 2 though", MaxSize, "will be tested.")

# Ask for the Multiplier, the y in yx+1

Multiplier = int(input("\nEnter a multiplier. For example 3, 5, 7, etc..: "))

# Ask how many iterations to go through when testing each x in yx+1
MaxIterations = int(input("\nEnter when to begin Logging Large Maximum iterations count: "))

# Ask if an optional time check is to be done at 1 second of processing time

TimeCheck = input("\nCheck the timer at 1 second to see how many numbers have been checked (y = yes)? ")
if TimeCheck == "y":
    StartTime = time.time()
    NumCount = 0

""" Set some variables
    > Set the start x in yx+1 to 2 (TestNum)
    > Set the number od loops found to 0 (LoopNum)
    > LoopControl determines if a new loop was found
"""
TestNum = 2
LoopNum = 0
LoopControl = 0

# Continue processing asl long as TestNum is less than or equal to the
# maximum allowable integer in Python
while TestNum <= MaxSize:

    """ Some variables that need to be set / reset before the interior while loop
        > Make Num equal to TestNum to retain TestNum value between each loop
        > Clear the MasterList array - a listing of all Num calculated
        > Clear the LoopList array - a list of all Num that appear in a loop
        > Reset the iteration counter (i)
    """
    Num = TestNum
    MasterList = []
    LoopList = []
    i = 0

    # Stay in the inside while loop as long as the iteration count
    # is less than MaxIterations and while LoopList has a length of 0.
    while i <= (MaxSize * 100) and len(LoopList) == 0:

        # Do a 1 second time check if TimeCheck is y
        if TimeCheck == "y":
            NumCount += 1
            CheckTime = int(time.time() - StartTime)
            if CheckTime == 1:
                print("\n", NumCount, "total numbers have been checked in the first second")
                Pause = input("\nPress Enter to continue...")

        # If Num isn't in MasterList, add it and process it
        if Num not in MasterList:

            # increment the iteration counter (i)
            i += 1

            # Add Num to MasterList
            MasterList.append(int(Num))

            print("Equation :(", Multiplier, "x)+1, inc =", i, "Testing:", TestNum, "Result:", int(Num))
            
            # If Num is even, divide by 2
            if Num % 2 == 0:
                Num = Num / 2

            # Else Num is odd then apply yx+1 formula it
            else:
                Num = Num * Multiplier + 1

        # If Num is in MasterList, use list comprehension to make the LoopList.
        # by taking the range of numbers from the first time Num appeared
        # in MasterList until the the end of MasterList
        else:
            LoopNum += 1
            LoopList = [MasterList[Index] for Index in range(MasterList.index(Num), len(MasterList))]

    """ END OF INSIDE while LOOP """
    
    """ Print any loops that are found into the log file -- but only if
        LoopNumber is greater than LoopControl

        > The log file is opened in append mode
        > The system's stdout (sys.stdout), normally to the terminal screen, is
          redirected to the log file
        > A line is printed
        > stdout is returned to the system's normal stdout
    """

    #with open(LogFile, 'a') as f:
    #    sys.stdout = f

    if LoopNum > LoopControl:
        with open(LogFile, 'a') as f:
            sys.stdout = f
            LoopControl = LoopNum
            print("(", Multiplier, "x+1) Testing:", TestNum, " Loop #", LoopNum, " Iteration", i, ":", LoopList)
            sys.stdout = original_stdout

    if i > MaxIterations:
        with open(LargeFile, 'a') as f:
            sys.stdout = f
            print("(", Multiplier, "x+1) Testing:", TestNum, " loop found at:", i, "above Max Iterations =", MaxIterations)

            sys.stdout = original_stdout

    #sys.stdout = original_stdout
    # Increment to the next number
    TestNum += 1

""" END OF OUTSIDE while LOOP """
