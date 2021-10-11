#!/bin/bash
#
# Filename: 3X+1.sh [renamed to yx+1 (or just yx)]
# Author: Jonathan Heard [with some modifications by Tracy]
# Purpose: Review the Collatz (3X+1) math challenge. 
# Pass the program the number when starting.
#
# Set initial varialbles
# i is the iteration counter
i=1

# Keeping track of Odds and Evens
Odd=0; Even=0

# Making sure Seed is blank
Seed=""

# Declaring arrays for loop detection.
# MasterList is an array that stores all numbers
# LoopList is an array that stores the numbers in a loop
# j is the counter to control LoopList elements
# k is the counter to control MasterList entries
MasterList=(); LoopList=(), j=0; k=0

# If log is passed on the command line, write output to yx.log
# By default, do not write to yx.log
LOG=no

# End of Variables

# Just a simple function to create blank lines
function BL
{
	echo; echo
}

# A function to output to screen and maybe the yx.log file
function Output ()
{
	if [[ $LOG != "yes" ]]
	then
		echo; echo $1
	else
		echo; echo $1 | tee -a yx.log
	fi
}

clear

# If log is passed form the command line, set LOG to yes to write to yx.log
if [[ $1 == "log" ]]
then
	LOG=yes
fi

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
	echo; echo "(3) 3x+1"
	echo "    [loop found]"
	echo "    4 2 1                             (seeds: all integers[?])"
	echo; echo "(5) 5x+1"
	echo "    [loops found]"
	echo "    26 13 66 33 166 83 416 208 104 52 (seeds: 5, 10, 13)"
	echo "    17 86 43 216 108 54 27 136 68 34  (seeds: 17)"
	echo "    8 4 2 1 6 3 16                    (seeds: 2, 3, 4, 6, 8, 12)"
	echo "    may not loop                      (seeds: 7, 9, 11, 14, 18)"
	echo; echo "(7) 7x+1"
	echo "    [loops found]"
	echo "    8 4 2 1                           (seeds: 2, 4, 5, 8, 9, 10, 19)"
	echo "    may not loop                      (seeds: 3, 6, 7)"
	echo; echo "(9) 9x+1"
	echo "    [loops found]"
	echo "    may not loop                      (seeds: all integers[?])"
	echo; echo "(Z) Exit the script."

	echo; read -n1 -p "Choose 3, 5, 7, 9 or Z: " Multiplier

	case $Multiplier in
		3 | 5 | 7 |9) break ;;
		z | Z) echo; exit 1 ;;
		*) BL; echo ">>>>> Please enter A, B, C, D, or Z! <<<<<"; echo
	esac
done

# Get the Seed (starting number)
while :
do
	BL; echo "(${Multiplier}x+1) Please enter a positive seed number"
	read -p "(press enter for a random number): " Seed

	# If user pressed enter at the prompt, assign a random number to Seed
	if [[ $Seed == "" ]]
	then
#		Seed=$RANDOM  ## This is limited to a max of 32768
		while [[ $Seed -le 0 ]]
		do
			Seed=$(od -An -N4 -i < /dev/urandom | tr -d ' ')
		done
		echo; echo "The random number chosen is: $Seed"
	fi

	if [[ $Seed -gt 0 ]]
	then
		echo; break
	else
		BL; echo ">>>>> I said enter a positive number! <<<<<"; echo
	fi
done

# Ask user: How iterations, default is 100
Iterations=""
echo; echo "Enter the number of iterations to run. Script will automatically stop if a loop is found."
read -p "(press Enter for the default of 100): " Iterations
if [[ $Iterations == "" ]]
then
	Iterations=100
fi

### Assign Seed to Num and to Max
# Seed will be maintained for future use.
# Num will be used for processing.
# Set Max here, too -- in case the Seed *is* the greatest number in the sequence
Num=$Seed; Max=$Seed

# Just an interesting thing. Checking to see if 3x+1 was chosen
# and if the Num being processed is a power of 2
if [[ Multiplier -eq 3 ]]
then
	echo
	if [[ $(($Seed & $Seed-1)) == 0 ]]
	then
	        echo "The Seed, $Seed, is a power of 2."
		echo "As a result, there will be no odd numbers."
	else
	        echo "The Seed, $Seed, is not a power of 2."
		echo "The result will be odd and even numbers."
	fi
	echo; read -n1 -p "Press enter to continue "
fi

echo

while :
do
	TempNum=$Num

	# Determine if Num is odd or even
	if [[ $(($Num%2)) == 0 ]]
	then
	
		# Do this stuff if it is even
		Num=$((Num/2))
		echo "Iteration # $i : $TempNum is even: $TempNum/2 = $Num"
		((Even++))

	else
		# Do this stuff if it is odd
		Num=$(((Num*$Multiplier)+1))
		echo "Iteration # $i : $TempNum is odd: ${Multiplier}x$TempNum+1 = $Num"
		((Odd++))
	fi

	# Keep track of the greatest number calculated
	if [[ $Num -gt $Max ]]
	then
		Max=$Num
	fi

	## Loop Detection
	if [[ $Iterations != "" ]]
	then
		# If Num is already in MasterList, a loop was found
		if [[ ${MasterList[*]} =~ $(echo "\<$Num\>") ]]
		then
			# If the Num exists in LoopList, break out, because we've just
			# discovered where the loop restarts. Otherwise, add it to LoopList
			if [[ ${LoopList[*]} =~ $(echo "\<$Num\>") ]]
			then
				break
			else
				LoopList[$j]=$Num; ((j++))
			fi
		fi
		
		# Add Num to MasterList
		MasterList[$k]=$Num; ((k++))
	fi

	# If Num is negative, break
	if [[ $Num -lt 0 ]]
	then
		BL; echo "Breaking due to a negative number."; break
	fi
	
	# If increment hits $Iterations, break
	if [[ $Iterations != "" ]]
	then
		if [[ $i -eq $Iterations ]]
		then
			BL; echo "Hit $Iterations iterations, exiting."; echo
			break
		fi
	fi
	
	((i++))
done

# Some statistics
Output "Equation: ${Multiplier}x+1"
Output "Initial Number = $Seed"
echo; echo "Largest Number = $Max"
echo; echo "Total iterations = $i"
echo; echo "There were $Even even numbers ($(echo "scale=3; $Even/$i*100" | bc)%) and $Odd odd ($(echo "scale=3; $Odd/$i*100" | bc)%) numbers."

# If j is not equal to 0, a loop was found
if [[ $j -gt 0 ]]
then
	Output "A loop was found! (${LoopList[*]})"
	Output "MasterList[] is:  (${MasterList[*]})"
else
	Output "No loop was discovered."
fi

if [[ $LOG == "yes" ]]
then
	echo "--------------------" >> yx.log
fi

echo

#
# End of file
#