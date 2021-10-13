#!/bin/python3

# Eventually, this will write to a file. So, sys is needed
# also, "copy" stdout to orginal_stdout. This will allow
# redirection of stdout to a file using print()
import sys
original_stdout = sys.stdout

# os needs to be imported to delete the log file, if it exists. 
# Otherwise, it just continues to grow with each execution of the script
import os
if os.path.exists('findloops.py.log'):
    os.remove('findloops.py.log')

# Ask for the Multiplier, the y in yx+1
Multiplier = int(input("\n\nEnter a multiplier. For example 3, 5, 7, etc..: "))

# Because it does not appear that this Python script will generate a negative
# integer (like Bash), ask how many iterations to go through when testing each x
# in yx+1
MaxIterations = int(input("\n\nMaximum iterations to test: "))

### Set some variables
# Set the start x in yx+1 to 2 (TestNum)
# Set the number od loops found to 0 (LoopNum)
# LoopControl determines if a new loop was found
TestNum = 2
LoopNum = 0
LoopControl = 0

while True:

    ### Some variables that need to be set / reset before the interior while loop
    # Make Num equal to TestNum to retain TestNum value between each loop
    # Clear the MasterList array - a listing of all Num calculated
    # Clear the LoopList array - a list of all Num that appear in a loop
    # Reset the iteration counter (i)
    Num = TestNum
    MasterList=[]
    LoopList=[]
    i = 0

    # It appears that Python isn't generating negative numbers. As a result, some
    # control needs to be put on this inside while loop. while True: could be used
    # to make it an infinite loop.
    while i < MaxIterations:

        # increment the iteration counter (i)
        i += 1
        
        # If Num is even, divide by 2
        if Num % 2 == 0:
            Num = Num / 2

        # If Num is odd then apply yx+1 formula it
        else:
            Num = Num * Multiplier + 1

        # Check to see if Num is already in the MasterList array
        if Num in MasterList:

            # If Num is already in LoopList, the loop is found
            # break the while loop
            if Num in LoopList:
                LoopNum += 1
                break
    
            # Otherwise, add Num to LoopList
            else:
                LoopList.append(int(Num))

        # Add Num to MasterList
        MasterList.append(int(Num))

        # If Num has gone negative, break out of the loop
        # This code section wasn't removed in case it is found,
        # at a later time, that Python does generate negative
        # numbers
#        if Num < 0:
#            print ("\n Num went negative.")
#            break

        # Print progress to screen
        print("Equation :(",Multiplier,"x+1) i =",i,"Testing:",TestNum,"Result:",int(Num))

    ##### END OF INSIDE while LOOP #####
    
    # Print any loops that are found into the log file -- but only if
    # LoopNumber is greater than LoopControl
    ### Note that:
    #   The log file is opened in append mode
    #   The system's stdout (sys.stdout), normally to the terminal screen, is
    #       redirected to the log file
    #   A line is printed
    #   stdout is returned to the system's normal stdout
    if LoopNum > LoopControl:
        LoopControl = LoopNum
        with open('findloops.py.log','a') as f:
            sys.stdout = f
            print ("(",Multiplier,"x+",TestNum,") Loop #",LoopNum,"at iteration",i,":",LoopList)
            sys.stdout = original_stdout

    # Increment to the next number
    TestNum += 1

##### END OF OUTSIDE while LOOP #####