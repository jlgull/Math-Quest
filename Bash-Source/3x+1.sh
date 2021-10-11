#!/bin/bash
#
# Filename: 3X+1.sh
# Author: Jonathan Heard
# Purpose: Review the Collatz (3X+1) math challenge. 
# Pass the program the number when starting.
#
# Set initial varialbles
# i is the iteration counter

i=0

# Max is the maximum value seen in $Num

Max=0

# End of Variables

Num=$1

clear; echo "Initial Number = $Num"; echo

while [[ $Num != 1 ]]

do
	if [[ $(($Num%2)) == 0 ]]
	then
		Num=$(($Num/2))
	else
		Num=$((($Num*3)+1))
	fi
	((i++))

	echo "Iteration # $i : Num = $Num"

	if [[ $Num -gt $Max ]]
	then

# Revised line, per comment from Tracy Baker.

#		Max=$(($Num))
		Max=$Num
	fi

done

echo; echo "Initial Number = $1"

echo; echo "Largest Number = $Max"

echo; echo "Total iterations = $i"


#
# End of file
#
