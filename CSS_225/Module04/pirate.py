# Author: Ishrak Rahman < admin@ishrak.xyz > 
# Last Edited: 5/6/2025
#
# Description
# Check input for "Arrr!". If found tell user to go away

greeting = input("Hello, possible pirate! What's the password? ")

if greeting in ["Arrr!"]:
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")
