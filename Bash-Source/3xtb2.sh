#!/bin/bash
#
# Filename: 3X+1.sh
# Author: Jonathan Heard [with some modifications by Tracy]
# Purpose: Review the Collatz (3X+1) math challenge. 
# Pass the program the number when starting.
#
# Set initial varialbles
# i is the iteration counter
i=1

# Max is the maximum value seen in $Num
Max=0

# Keeping track of Odds and Evens
Odd=0; Even=0

# Making sure Seed is blank
Seed=""

# End of Variables

clear

read -p "Please enter a seed number (press enter for a random number): " Seed; echo

# If user pressed enter at the prompt, assign a random number to Seed
if [[ $Seed == "" ]]
then
	Seed=$RANDOM
fi

### Assign Seed to Num
# Seed will be maintained for future use.
# Num will be used for processing.
Num=$Seed

while [[ $Num != 1 ]]
do
	TempNum=$Num	

	# Determine if Num is odd or even
	if [[ $(($Num%2)) == 0 ]]
	then
	
	# Do this stuff if it is even
		Num=$((Num/2))
		echo "Iteration # $i : $TempNum is even: $TempNum/2 = $Num"
		((Even++))

	# Do this stuff if it is odd
	else
		Num=$(((Num*3)+1))
		echo "Iteration # $i : $TempNum is odd: 3x$TempNum+1 = $Num"
		((Odd++))
	fi
	
	# Only increment if Num > 1
	# otherwise,  the final increment is off by 1
	if [[ $Num -gt 1 ]]
	then
		((i++))
	fi

	# Keep track of the greatest number calculated
	if [[ $Num -gt $Max ]]
	then
		Max=$Num
	fi

done

# Some statistics
echo; echo "Initial Number = $Seed"
echo; echo "Largest Number = $Max"
echo; echo "Total iterations = $i"
echo; echo "There were $Odd odd numbers and $Even even numbers. $(echo "scale=4; $Even/$i*100" | bc)% were even and $(echo "scale=4; $Odd/$i*100" | bc)% were odd."

#
# End of file
#
