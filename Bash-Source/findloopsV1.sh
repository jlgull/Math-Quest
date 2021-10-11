#!/bin/bash

##### Ya, ya... written by Tracy Baker on a whim.

# Print the usage statement
if [[ $1 == "" ]]
then
	clear
	echo; echo "Run the script as findloops <multiplier>"
	echo; echo "<multiplier> may be any number. Only odd numbers will find loops."
	echo; echo "Good numbers to try are 5, 7, 15, 31, 63, 127, 255, ..."
	echo; echo "A minimal log file is generated showing the equation, the numbers that"
	echo "generated a loop, and the loop it created."
	echo; echo "The findloops.log file can be followed with:"
	echo "tail -f findloops.log (use Ctrl+c to stop following)"
	exit 1
fi

##### Set default variables:
# Multiplier is the value passed to the script, used as the y in yx+1
# TestNum is the number current being tested
# Loop couts the number of loops that have been found
# logfile is the log file to write to

Multiplier=$1; TestNum=2; Loop=0; logfile="findloops.log"

clear

# Start logfile - write the formula being using (yx+1)
echo > $logfile
echo "Equation: ${Multiplier}x+1" >> $logfile
echo "-------------------" >> $logfile
echo "Legend: <number being tested> [i=<number of iterations used to find loop>, #<loop number>]: (<loop members>)" >> $logfile
echo "-------------------" >> $logfile

# Start the outside loop. It will continue while $TestNum is a positive number
# this ensures that all numbers will get tested - 2 through 9,223,372,036,854,775,807.
# This means the script will, in essence, never stop because we will never live long
# enough to see the end -- because at one calculation per second, it'll take 
# 292,271,023,045.31 years to finish. Of course, even if it is doing 10, or 100, or
# 1,000 per second, we'll still not live long enough to see the end.

while [[ $TestNum -gt 0 ]]
do
	#### Initialize variables used for each number being tested
	# Num is used for processing, to preserve the number being tested
	# MasterList() is an array to keep all of the numbers being generated
	# LoopList() is an array used to keep the numbers in a loop (if any)
	# i is used to keep track of the iterations that each number goes through
	# m increments the index in the MasterList() array
	# l increments the index in the LoopList() array

	Num=$TestNum; MasterList=(); LoopList=(); i=0; l=0; m=0

	# The inside loop, where the processing takes place. This loop will break
	# (on purpose) if [1] a loop is found or [2] Num goes negative
	while :
	do
		# Incerment the . . . increment
		((i++))

		# Test for odd or even
		if [[ $(($Num%2)) == 0 ]]
		then
			# If even, divide by 2 and put back into Num
			Num=$((Num/2))
		else
			# If odd, apply yx+1 and put back into Num
			Num=$(((Num*$Multiplier)+1))
		fi

		# If Num is already in MasterList, a loop was found
		if [[ ${MasterList[*]} =~ $(echo "\<$Num\>") ]]
		then
			# Check to see if Num is in the LoopList array
			if [[ ${LoopList[*]} =~ $(echo "\<$Num\>") ]]
			then
				# If it is, the loop is complete. Iincrement
				# the Loop counter and break out of the inside while loop
				((Loop++)); break
			else
				# If it isn't, the loop isn't finished building,
				# so add Num to end of LoopList array
				LoopList[$l]=$Num; ((l++))
			fi
		fi
		
		# Add Num to MasterList
		MasterList[$m]=$Num; ((m++))

		# If Num is negative, break out of the inside while loop
		if [[ $Num -lt 0 ]]
		then
			break
		fi
	done

	# If l is not equal to zero a loop was found
	if  [[ $l != 0 ]]
	then
		#### A loop was found, print to screen and findloops.log ($logfile):
		# the number being processed ($TestNum)
		# how many iterations the inside while loop used ($i)
		# the loops number ($Loop)
		# loop members (${LoopList[*]})
		echo "$TestNum [i=$i, #$Loop]: (${LoopList[*]})" | tee -a $logfile
	else
		
		#### A loop was NOT found, print to screen only:
		# the number being processed ($TestNum)
		# how many iterations the inside while loop used ($i)
		echo "$TestNum [i=$i]"
	fi

	# increment TestNum -- time to do the next one!
	((TestNum++))
done

# print the total number of loops found to findloops.log ($logfile)
# Again, it'll never get here because there just isn't enough time.
echo "${Loop}s were found." >> $logfile

echo; echo "Finished!"

#### EOF