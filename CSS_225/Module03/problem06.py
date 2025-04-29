# Author: Ishrak Rahman < admin@ishrak.xyz >
# Last Edited: 4/29/2025
# 
# Description:
# A scrpt that converts the temperature from Farenheit to Celcius

#!/usr/bin/env python

temp_in_farenheit = float(input("Please enter the temperature in Farenheit: "))
temp_in_celsius = ((temp_in_farenheit - 30) / 2)
print(temp_in_celsius)