# Author: Ishrak Rahman < admin@ishrak.xyz > 
# Last Edited: 5/6/2025
#
# Description: 
# Converts inputs from string to integer then adds the second input. The result is printed.

time_str = input("What time is it now? ")
wait_time_str = input("What is the number of nours to wait? ")

time_int = int(time_str)
wait_time_int = int(wait_time_str)

time_when_alarm_go_off = time_int + wait_time_int
print("The alarm will go off at: ", time_when_alarm_go_off)
