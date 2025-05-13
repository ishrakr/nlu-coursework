# Author: Ishrak Rahman < admin@ishrak.xyz > 
# Last Edited: 5/6/2025
#
# For multiples of three print “Divisible by three” instead of the number and for the multiples of five print “Divisible by five”. For numbers which are multiples of both three and five print “Divisible by both”. 

for i in range(1, 51):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i, "is divisible by both")
    elif i % 3 == 0:
        print(i, "is divisible by three")
    elif i % 5 == 0:
        print(i, "is divisible by five")