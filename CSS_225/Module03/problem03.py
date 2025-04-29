# Author: Ishrak Rahman < admin@ishrak.xyz >
# Last Edited: 4/29/2025
# 
# Description:
# A script that only lets authorized people into CSS-225 class

#!/usr/bin/env python
user_input = input ("Enter username:")
allowed_users = ["Ishrak", "Akshay", "Fatima"]

if user_input in allowed_users:
    print("✅ Welcome to CSS 225!")
else:
    print("🛑 You are not allowed!")

