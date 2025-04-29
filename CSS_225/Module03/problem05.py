# Author: Ishrak Rahman < admin@ishrak.xyz >
# Last Edited: 4/29/2025
# 
# Description:
# A script that calculates the miles per gallon of your trip

#!/usr/bin/env python

miles = float(input("Please enter the miles driven: "))
gas = float(input("How many gallons of gas used?: "))

mpg = (miles / gas)

print("Miles per Gallon:", mpg)