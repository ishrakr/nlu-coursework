# Author: Ishrak Rahman < admin@ishrak.xyz >
# Last Edited: 4/17/2025
# 
# Description:
# A python script that checks username and grants access based on an allowed list

#!/usr/bin/env python

username = input ("Enter username: ")
allowed_users = ["Ishrak", "Akshay", "Fatima"]

if username in allowed_users:
    print("Allowed")
else:
    print("Denied")