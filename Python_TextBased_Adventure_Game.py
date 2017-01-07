print('''
TextBased Adventure Game
by Gerrit Ohrner
''')
#To do
#0.5. Texte erscheinen lassen, wenn man den Raum wechselt, welche einem sagen wie das momentane Ambiente ist. DONE
#1. Groesse des Feldes variabel halten. (3x3, 4x4, 5x5, etc.)
#2. Groesse laesst sich via "Schwierigkeitsgrad" verändern. Gucken ob Schwierikgeitsgrad das richtige wort ist. Vielleicht einfach groesse.
#3. Random Waende aufstellen lassen. (Menge der Waende je nach größe auswaehlen koennen)
#4. minimalistisches kampfsystem? halb DONE
#5. Stimmungsstufen für die antwortende "Stimme(Der Text den der Spieler ließt)". Je nach Aktionen werden die gesprochenen Texte netter oder unfreundlicher.

import random
import os # os.system('cls' if os.name == 'nt' else 'clear') ///to clear the terminalscreen
os.system('cls' if os.name == 'nt' else 'clear')
filePath = os.path.dirname(os.path.abspath(__file__)) #Saves the path where the script is running in the variable filePath
with open(filePath + '\\wrong_input.txt', "r") as I:
	content_input = I.readlines()
with open(filePath + '\\hittin_walls.txt', "r") as H:
	content_walls = H.readlines()
with open(filePath + '\\change_rooms.txt', "r") as R:
	content_rooms = R.readlines()
Iinput = 0
Winput = 0
Rinput = 0
rcounter = 5
rcounterBackup = 0
direction = ""
health = 100
mana = 100
difficultySet = 0
difficulty = 0

while difficultySet == 0:
	print('1. Easy')
	print('2. Medium')
	print('3. Hard')
	difficultySet = int(input('Please select difficulty (1/2/3):'))
	if difficultySet < 1:
		print('Out of range!')
		difficultySet = 0
	elif difficultySet > 3:
		print('Out of range!')
		difficultySet = 0
#	print(difficultySet)
	if difficultySet == 1:
		difficultySet = 10
	elif difficultySet == 2:
		difficultySet = 5
	elif difficultySet == 3:
		difficultySet = 2
os.system('cls' if os.name == 'nt' else 'clear')

def interface():
	global health
	global mana
	rooms()
	events()
	print('Status:')
	print('Health =', health)
	print('Mana =', mana, '\n')

def rooms():
	global rcounter
	global rcounterBackup
	global Rinput
	print("Dungeon-Layout:")
	if rcounter == 1:
		print(' 7 8 9\n 4 5 6\n(1)2 3\n')
	elif rcounter == 2:
		print(' 7 8 9\n 4 5 6\n 1(2)3\n')
	elif rcounter == 3:
		print(' 7 8 9\n 4 5 6\n 1 2(3)\n')
	elif rcounter == 4:
		print(' 7 8 9\n(4)5 6\n 1 2 3\n')
	elif rcounter == 5:
		print(' 7 8 9\n 4(5)6\n 1 2 3\n')
	elif rcounter == 6:
		print(' 7 8 9\n 4 5(6)\n 1 2 3\n')
	elif rcounter == 7:
		print('(7)8 9\n 4 5 6\n 1 2 3\n')
	elif rcounter == 8:
		print(' 7(8)9\n 4 5 6\n 1 2 3\n')
	elif rcounter == 9:
		print(' 7 8(9)\n 4 5 6\n 1 2 3\n')

def events():
	global rcounter
	global rcounterBackup
	global Rinput
	print('Current events:')
	if rcounter != rcounterBackup:
		if Rinput == 0:
			print(content_rooms[0])
			Rinput = Rinput + 1
		elif Rinput < len(content_rooms):
			print(content_rooms[Rinput])
			Rinput = Rinput + 1
		elif Rinput >= len(content_rooms):
			print("It smells horrible here. Maybe a troll is arround the corner?\n")
			Rinput = 0
		else:
			print('None\n')

	
#	if rcounter == rcounterBackup;
		

def fight():
	print("Current fights:")
	global health
	global mana
	global difficultySet
	difficulty = random.randint(1, difficultySet)
	if difficulty == 1:
		print('von einem Troll getrollt!')
		print('Health - 10\n')
		health = health - 10
	else:
		print('No fiends in sight!\n')
	
	if health <= 0:
		print('Game over!\nYou suck M8!')
		input()
		exit()

def movement():
	global rcounter
	global rcounterBackup
	global direction
	direction = input('In which direction do you want to move?(north/east/south/west)')
	rcounterBackup = rcounter
	if direction == "north":
		rcounter = rcounter + 3
	elif direction == 'east':
		if rcounter == 3 or rcounter == 6:			
			hittin_walls()
		else:
			rcounter = rcounter + 1
	elif direction == 'south':
		rcounter = rcounter - 3
	elif direction == 'west':
		if rcounter == 4 or rcounter == 7:
			hittin_walls()
		else:
			rcounter = rcounter - 1
	elif direction == 'exit':
		print('Hey, you found the Exit ;-)')
	else:
		wrong_input()
		
	if rcounter < 1:
		hittin_walls()
	elif rcounter > 9:
		hittin_walls()

	
def hittin_walls():
	global rcounter
	global Winput
	rcounter = rcounterBackup
#	print('Schleifenanfang', Winput)
	if Winput == 0:
		print(content_walls[0])
		Winput = Winput + 1
	elif Winput < len(content_walls):
		print(content_walls[Winput])
		Winput = Winput + 1
	elif Winput >= len(content_walls):
		print("I guess I will show you a trick. Maybe then you will stop doing that")
		Winput = 0
		teleport()
#	print('Schleifenende', Winput)

def teleport():
	global direction
	global rcounter
	if direction == "north":
		rcounter = rcounter - 6
	elif direction == 'east':
		rcounter = rcounter - 2
	elif direction == 'south':
		rcounter = rcounter + 6
	elif direction == 'west':
		rcounter = rcounter + 2
	else:
		wrong_input()

def wrong_input():
	global Iinput
#	print('Schleifenanfang', Iinput)
	if Iinput == 0:
		print(content_input[0])
		Iinput = Iinput + 1
	elif Iinput < len(content_input):
		print(content_input[Iinput])
		Iinput = Iinput + 1
	elif Iinput >= len(content_input):
		print("This is only gonna go back to the start")
		Iinput = 0
		# Wenn man leben hat, hier vielleicht bei zu vielen falschen Eingeben Leben abziehen.
	
while direction != "exit":
	interface()
	fight()
	movement()
#	print('Codeende', Winput)
	input()
	os.system('cls' if os.name == 'nt' else 'clear')