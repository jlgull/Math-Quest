#!/bin/bash
#
# Filename: 3X+1.sh [renamed to yx+1]
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

# Making sure Seed and Delay are blank
Seed=""; Delay=""

# End of Variables

# Just a simple function to create blank lines
function BL
{
	echo; echo
}

clear

# Testing some other "yx+1" scenarios. Note that y must be odd
# 
# if y is even, the result will eventually be odd and neverending
# for example:
#
# Begin with 3 (odd)  -> 2(3)+1 = 7  -> 2(7)+1  = 15 -> 2(15)+1 = 31, etc.
# Begin with 5 (odd)  -> 2(5)+1 = 11 -> 2(11)+1 = 23 -> 2(23)+1 = 47, etc.
# Begin with 4 (even) -> 4/2    = 2  -> 2/2     = 1  -> 2(1)+1  = 3 -> 2(3)+1 = 7, etc.
#
# Begin with 3 (odd)  -> 4(3)+1 = 13 -> 4(13)+1 = 53 -> 4(15)+1 = 213, etc.
# Begin with 5 (odd)  -> 4(5)+1 = 21 -> 4(21)+1 = 85 -> 4(85)+1 = 341, etc.
# Begin with 4 (even) -> 4/2    = 2  -> 2/2     = 1  -> 4(1)+1  = 5 -> 4(5)+1 = 21, etc.

while :
do
	echo "Choose which to run:"
	echo; echo "(3) 3x+1 [ends with looping 4,2,1]"
	echo; echo "(5) 5x+1 [ends with looping 66,33,166,83,416,208,104,52,26,13  OR  4,2,1  OR  may not loop]"
	echo; echo "(7) 7x+1 [probably doesn't loop]"
	echo; echo "(9) 9x+1 [probably doesn't loop]"
	echo; echo "(Z) Exit the script."

	echo; read -n1 -p "Choose 3, 5, 7, 9 or Z: " Multiplier

	case $Multiplier in
		3 | 5 | 7 |9) break ;;
		z | Z) echo; exit 1 ;;
		*) BL; echo ">>>>> Please enter A, B, C, D, or Z! <<<<<"; echo
	esac
done

# The following represent the ending digit(s) for 3x+1 --
# and 7x+1 and 9x+1, because they probably don't loop
EndNum1=1; EndNum2=1

# Only ask to set limit is formula is *not* 3x+1
if [[ $Multiplier -ne 3 ]]
then
	# Set Limits? If so and if 5x+1, use 1 and 13
	# Otherwise let it run to 50,000 iterations, looking for patterns
	# by setting EndNum1 and EndNum2 to 0
	BL; echo "Set limits [y = yes, n = let it run for 50,000 iterations, looking for patterns]?"
	read -n1 -p "(7x+1 and 9x+1 will probably go to 50,000 anyway as they don't appear to loop): " Choice
	if [[ $Choice == "y" && $Multiplier -eq 5 ]]
	then
		EndNum1=1; EndNum2=13
	else
		EndNum1=0; EndNum2=0
	fi

fi

# Get the Seed (starting number)
BL; read -p "(${Multiplier}x+1) Please enter a seed number (press enter for a random number): " Seed
echo

# If user pressed enter at the prompt, assign a random number to Seed
if [[ $Seed == "" ]]
then
	Seed=$RANDOM
	echo; echo "The random number chosen is: $Seed"
fi

### Assign Seed to Num
# Seed will be maintained for future use.
# Num will be used for processing.
Num=$Seed

# Ask the user if they want a delay, Enter = no
echo; read -n1 -p "Do you want a 1 second delay between interations? (default is no, y = yes): " Delay

while [[ $Num != $EndNum1 && $Num != $EndNum2 ]]
do
	# If increment hits 50,000, go ahead and exit
	if [[ $i -gt 50000 ]]
	then
		BL; echo "Hit 50,000 iterations, exiting."; echo
		((i--))
		break
	fi
	
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
		Num=$(((Num*$Multiplier)+1))
		echo "Iteration # $i : $TempNum is odd: ${Multiplier}x$TempNum+1 = $Num"
		((Odd++))
	fi
	
	# Only increment if Num is not equal to EndNum1 and EndNum2
	# otherwise, the final increment is off by 1
	if [[ $Num -ne $EndNum1 && $Num -ne $EndNum2 ]]
	then
		((i++))
	else
		if [[ $Multiplier -eq 5 ]]
		then
			echo; echo "The result is $Num, one of the ending numbers for 5x+1."
		else
			echo; echo "The result is equal to 1, the end has been reached."
		fi
	fi

	# Keep track of the greatest number calculated
	if [[ $Num -gt $Max ]]
	then
		Max=$Num
	fi

	if [[ $Delay == "y" ]]
	then
		sleep 1
	fi

done

# Some statistics
echo; echo "Initial Number = $Seed"
echo; echo "Largest Number = $Max"
echo; echo "Total iterations = $i"
echo; echo "There were $Even even numbers ($(echo "scale=3; $Even/$i*100" | bc)%) and $Odd odd ($(echo "scale=3; $Odd/$i*100" | bc)%) numbers."

#
# End of file
#