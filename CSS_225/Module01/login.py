# Author: Ishrak Rahman
# Last Edited: 4/13/2025
# 
# Description:
# A python script to function as an access control system.

#!/usr/bin/env python

# Take username as input from the user
username = input("Login: >> ")

# Fixed variable set for user1 as Jack
user1 = "Jack"

# Fixed variable set for user2 as Jill
user2 = "Jill"

# If the user input matches user1, output a message.
if username == user1:
    print("Access granted")
# If the user input matches user2, output another message. 
elif username == user2:
    print("Welcome to the system")
# Fallback rule for unmatched names
else:
    print("Access denied")
