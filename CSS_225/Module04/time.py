# Author: Ishrak Rahman < admin@ishrak.xyz > 
# Last Edited: 5/6/2025
#
# Description: 
# Converts inputs from string to integer then adds the second input. The result is printed.

current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
print("The final time is: ", final_time_int)
