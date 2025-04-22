# Author: Ishrak Rahman < admin@ishrak.xyz >
# Last Edited: 4/17/2025
# 
# Description:
# A script that calculates your BMI index and tells you the status of your health based on it.

#!/usr/bin/env python

height = float(input("Please enter your height (Feet)"))
weight = int(input("Please enter your weight (Pounds)"))

bmi = weight / height

# Calculate BMI:
if (bmi < 18.5):
    print("You are underweight")
elif (bmi > 18.5) & (bmi < 24.9):
    print("You are in great shape!")
elif (bmi > 24.9) & (bmi < 29.9):
    print("You are overweight")
else:
    print("You are obese")