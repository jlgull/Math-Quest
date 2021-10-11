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

# End of Variables

Num=$1

clear; echo "Initial Number = $Num"; echo

while [[ $Num != 1 ]]
do
	TempNum=$Num	

	if [[ $(($Num%2)) == 0 ]]
	then
		Num=$(($Num/2))
		echo "Iteration # $i : $TempNum is even: $TempNum/2 = $Num"
		((++Even))
	else
		Num=$((($Num*3)+1))
		echo "Iteration # $i : $TempNum is odd: 3x$TempNum+1 = $Num"
		((++Odd))
	fi
	((i++))

	if [[ $Num -gt $Max ]]
	then
		### You had Max=$(($Num)) here. The parens are not needed
		### as no math is taking place.

		Max=$Num
	fi

done

echo; echo "Initial Number = $1"

echo; echo "Largest Number = $Max"

echo; echo "Total iterations = $i"

echo; echo "There were $Odd odd numbers and $Even even numbers."


#
# End of file
#