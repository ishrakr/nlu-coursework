# Author: Ishrak Rahman
# Last Edited: 4/13/2025
# 
# Description:
# This is a python script to convert speed from metric system (KMH) to imperial (MPH)
 
#!/usr/bin/env python

# Take input from the user as integer and set the variable kmh.
kmh = int(input("Enter km/h: "))

# Conversion to km/h by multiplication using known value
mph =  0.6214 * kmh

# Output the result
print("Speed:", kmh, "KM/H = ", mph, "MPH")
