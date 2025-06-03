import time

def start():
	global player_name
	print("Welcome to the game", player_name)

	time.sleep(1)

	print("Ready to begin? ")

	texts = ['...', '*ring* *ring*', 'Answer?',]
	for text in texts:
		print(text)
		time.sleep(1)
	
	user_input = input("Press Y to answer the phone ")

	if user_input == "Y":
		print('[YOU]: Hello?')
		time.sleep(1)
		print(f'[MOM]: {player_name}, its your grandma!')
		time.sleep(1)
		print('[MOM]: I dont know where she is gone')
		time.sleep(1)
		print('[MOM]: She was last seen in the kitchen')
		time.sleep(1)
		print('[MOM]: I need you to find her!')
		time.sleep(1)
		
		user_input = input("Press Y to find grandma ")
		
		if user_input == "Y":
			print('[You]: Okay, I will find her!')
			time.sleep(1)
			print('[You]: I dont know where to start...')
			time.sleep(1)
			checkpoint_1()

		else:
			print('Game Over!')
			return False
		
	else:
		print('Game Over!')

def checkpoint_1():
	print("Where should I go?")
	time.sleep(1)
	print("1. Check the Rooftop")
	print("2. Check the Garage")	
	
	user_input = input("Choose 1 or 2: ")
	
	if user_input == "1":
		check_rooftop()
	elif user_input == "2":
		check_garage()
	else:
		print("Invalid choice! Please choose 1 or 2.")
		checkpoint_1()

def check_rooftop():
	print("You chose to check the Rooftop.")

	time.sleep(1)

	print("Walking up the stairs, you reach the Rooftop.")

	time.sleep(1)

	user_input = input("Press F to look around: ")

	if user_input == "F":
		print("You find nothing there, but you hear a noise from the Staircase.")
		time.sleep(1)
		print("Investigate?")
		user_input = input("Press Y to investigate or N to ignore: ")
		if user_input == "Y":
			print("You decide to investigate the noise.")
			time.sleep(1)
			print("You find a cat sitting on the stairs, meowing loudly.")
			time.sleep(1)
			checkpoint_1()
		elif user_input == "N":
			print("You ignore the noise.")
			time.sleep(1)
			print("You dont find anything on the Rooftop.")
			checkpoint_1()
		else:
			print("Invalid input! You need to press Y or N.")
			checkpoint_1()
	else:
		print("Invalid input! You need to press F to look around.")
		check_rooftop()

def check_garage():
		print("You chose to check the Staircase.")
		time.sleep(1)
		print("Walking down the stairs, you reach the Garage.")
		time.sleep(1)
		user_input = input("Press F to look around: ")
		if user_input == "F":
			print("Looking around the Garage, you find some old tools and a car.")
			time.sleep(1)
			print("You notice her shoes lying on the floor.")
			time.sleep(1)
			print("[GAME]: YOU RECEIVED A CLUE: Grandma's shoes are in the Garage.")
			clue_found = 1
			time.sleep(1)
			print("What do you want to do next?")
			time.sleep(1)
			print("1. Return to the Rooftop")
			print("2. Talk to Mum")
			user_input = input("Choose 1 or 2: ")
			if user_input == "1":
				checkpoint_1()
			elif user_input == "2":
				talk_mum()
			else:
				print("Invalid choice! Please choose 1 or 2.")
				check_garage()

def talk_mum():
	print("In Progress...")
	time.sleep(1)

	print("Tell her about the shoes you found in the Garage?")	
	user_input = input("Press Y to tell Mum")
	if user_input == "Y":
		print("You tell Mum about the shoes you found in the Garage.")
		time.sleep(1)
		print("[MUM]: Oh, those are her favorite shoes!")
		time.sleep(1)
		print("[MUM]: She must be nearby, she never goes anywhere without them.")
		time.sleep(1)
		print("You feel a sense of relief knowing that Grandma is close by.")
		time.sleep(1)
		print("She must have gone outside... I should start checking the neighborhood!")
		
	else:
		print("I think you should tell Mum about the shoes.")
		talk_mum()	