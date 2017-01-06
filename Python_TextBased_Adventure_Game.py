print('''
TextBased Adventure Game
by Gerrit Ohrner
''')
#To do
#0.5. Texte erscheinen lassen, wenn man den Raum wechselt, welche einem sagen wie das momentane Ambiente ist.
#1. Groesse des Feldes variabel halten. (3x3, 4x4, 5x5, etc.)
#2. Groesse laesst sich via "Schwierigkeitsgrad" verändern. Gucken ob Schwierikgeitsgrad das richtige wort ist. Vielleicht einfach groesse.
#3. Random Waende aufstellen lassen. (Menge der Waende je nach größe auswaehlen koennen)
#4. minimalistisches kampfsystem?
#5. Stimmungsstufen für die antwortende "Stimme(Der Text den der Spieler ließt)". Je nach Aktionen werden die gesprochenen Texte netter oder unfreundlicher.


import os # os.system('cls' if os.name == 'nt' else 'clear') ///to clear the terminalscreen
os.system('cls' if os.name == 'nt' else 'clear')
filePath = os.path.dirname(os.path.abspath(__file__)) #Saves the path where the script is running in the variable filePath
with open(filePath + '\\wrong_input.txt', "r") as q:
	content_input = q.readlines()
with open(filePath + '\\hittin_walls.txt', "r") as y:
	content_walls = y.readlines()
Iinput = 0
Winput = 0
rcounter = 5
rcounterBackup = 0
direction = ""

def rooms(rcounter):
	if rcounter == 1:
		print(' 7 8 9\n 4 5 6\n(1)2 3')
	elif rcounter == 2:
		print(' 7 8 9\n 4 5 6\n 1(2)3')
	elif rcounter == 3:
		print(' 7 8 9\n 4 5 6\n 1 2(3)')
	elif rcounter == 4:
		print(' 7 8 9\n(4)5 6\n 1 2 3')
	elif rcounter == 5:
		print(' 7 8 9\n 4(5)6\n 1 2 3')
	elif rcounter == 6:
		print(' 7 8 9\n 4 5(6)\n 1 2 3')
	elif rcounter == 7:
		print('(7)8 9\n 4 5 6\n 1 2 3')
	elif rcounter == 8:
		print(' 7(8)9\n 4 5 6\n 1 2 3')
	elif rcounter == 9:
		print(' 7 8(9)\n 4 5 6\n 1 2 3')
	return rcounter

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
		print("Is jetzt groesser. Aus andere seite teleportieren")
		Winput = 0
		teleport()
#	print('Schleifenende', Winput)
	input()
	return

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
	#content_input
	global Iinput
#	print('Schleifenanfang', Iinput)
	if Iinput == 0:
		print(content_input[0])
		Iinput = Iinput + 1
	elif Iinput < len(content_input):
		print(content_input[Iinput])
		Iinput = Iinput + 1
	elif Iinput >= len(content_input):
		print("Is jetzt groesser. Aus andere seite teleportieren")
		Iinput = 0
#	print("Thats not a direction, you know?")
	input()
	
while direction != "exit":
	rooms(rcounter)
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
	else:
		wrong_input()
	if rcounter < 1:
		hittin_walls()
	elif rcounter > 9:
		hittin_walls()
#	print('Codeende', Winput)
	input()
	os.system('cls' if os.name == 'nt' else 'clear')

#while Winput <= len(content_walls):
#	print(content_walls[Winput])
#	Winput = Winput + 1
#	break