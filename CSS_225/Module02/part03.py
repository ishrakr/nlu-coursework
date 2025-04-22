# Author: Ishrak Rahman < admin@ishrak.xyz >
# Last Edited: 4/17/2025
# 
# Description:
# A script that takes two numbers and gives the user the option to calculate the sum or product.

#!/usr/bin/env python

num1 = int(input("Please enter First Number: "))
num2 = int(input("Please enter Second Number: "))

print ("Which calculation would you like to perform?")
print ("===============================================")
print ("Type A to calculate the Sum")
print ("Type B to calculate the product")
print ("===============================================")

user_choice = str(input("Please enter your choice: "))

if user_choice == "A":
    sum = num1 + num2
    print("The Sum is:", sum)
elif user_choice == "B":
    product = num1 * num2
    print("The Product is:", product)
else:
    print("Invalid Choice")