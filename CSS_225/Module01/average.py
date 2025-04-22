# Author: Ishrak Rahman
# Last Edited: 4/13/2025
# 
# Description:
# This is a python script to calculate the average score of between three rounds.

#!/usr/bin/env python

# Take input from the user for round 1
round1 = int(input("Enter score for round 1: "))

# Take input from the user for round 2
round2 = int(input("Enter score for round 2: "))

# Take input from the user for round 3
round3 = int(input("Enter score for round 3: "))

# Calculation of average and setting the results as the variable named average
average = (round1 + round2 + round3) / 3

# Print results to output.
print ("the average score is: ", average)
