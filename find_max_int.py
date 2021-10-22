#!/bin/python3

"""
Original findloop.py written by Tracy Baker

V2 rewritten with loop detection concepts from Jonathan Heard,
which only processes numbers if they aren't in the master number
list. Once a number is repeated, the loop number list can be
constructed.
"""

# Eventually, this will write to a file. So, sys is needed
# also, "copy" stdout to orginal_stdout. This will allow
# redirection of stdout to a file using print()
import sys
original_stdout = sys.stdout

# To allow for measuring time it takes to reach each new Max Iteration.

import time

# Set the log file name
LogFile = "findloops.py.log"

# os needs to be imported to delete the log file, if it exists. 
# Otherwise, it just continues to grow with each execution of the script
import os
if os.path.exists(LogFile):
    os.remove(LogFile)

print ("\nThe log file being used is:",LogFile)

print ("\nThe numbers 2 though {:,}".format(sys.maxsize), "will be tested.")
print ("(It'll take roughly 5 million years, at 100 iterations per number,")
print ("to check them all ... which is still about 40 times faster than Bash.)")

# Ask for the Multiplier, the y in yx+1
Multiplier = int(input("\nEnter a multiplier. For example 3, 5, 7, etc..: "))

# Ask how many iterations to go through when testing each x in yx+1
# MaxIterations = int(input("\nMaximum iterations to test (note loops have been found between 100 and 200): "))

""" Set some variables
    > Set the start x in yx+1 to 2 (TestNum)
    > Set the number od loops found to 0 (LoopNum)
    > LoopControl determines if a new loop was found
"""
TestNum = 2
Max_i = LoopControl = LoopNum = 0

# Create a variable to capture start time
StartTime = time.time()

# Continue processing asl long as TestNum is less than or equal to the
# maximum allowable integer in Python

# print ("\n\nRunning...")

while TestNum <= sys.maxsize:

    """ Some variables that need to be set / reset before the interior while loop
        > Make Num equal to TestNum to retain TestNum value between each loop
        > Clear the MasterList array - a listing of all Num calculated
        > Clear the LoopList array - a list of all Num that appear in a loop
        > Reset the iteration counter (i)
    """
    Num = TestNum
    MasterList=[]
    LoopList=[]
    i = 0

#    print ("Loops found:",LoopNum)

    # Stay in the inside while loop until either the maximum number
    # of iterations is reached or while LoopList has a length of 0.
    while i <= sys.maxsize and len(LoopList) == 0:

        # increment the iteration counter (i)
        i += 1

        # If Num isn't in MasterList, add it and process it
        if Num not in MasterList:
    
            # Add Num to MasterList
            MasterList.append(int(Num))
            
            # If Num is even, divide by 2
            if Num % 2 == 0:
                Num = Num / 2

            # If Num is odd then apply yx+1 formula it
            else:
                Num = Num * Multiplier + 1

        # If Num is in MasterList, a loop is found. Create LoopList
        # by taking the range of numbers from the first time Num appeared
        # in MasterList until the the end of MasterList
        else:
            LoopNum += 1
            for Index in range(MasterList.index(Num),len(MasterList)):
                LoopList.append(MasterList[Index])

        print("Equation :(",Multiplier,"x)+1, inc =",i,"Testing:",TestNum,"Result:",int(Num))

    """ END OF INSIDE while LOOP """
    
    """ Print any loops that are found into the log file -- but only if
        LoopNumber is greater than LoopControl

        > The log file is opened in append mode
        > The system's stdout (sys.stdout), normally to the terminal screen, is
          redirected to the log file
        > A line is printed
        > stdout is returned to the system's normal stdout
    """
    if LoopNum > LoopControl:
        LoopControl = LoopNum

        if i > Max_i:
            with open(LogFile,'a') as f:
                sys.stdout = f
                print ("(", Multiplier, "x+1) Testing:", TestNum,
                       " Max. Iteration", Max_i, " @ {:6.2f}".format(time.time()-StartTime), " Seconds"),
                sys.stdout = original_stdout
            Max_i = i
    
    # Increment to the next number
    TestNum += 1

""" END OF OUTSIDE while LOOP """