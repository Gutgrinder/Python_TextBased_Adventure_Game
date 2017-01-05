print('''
TextBased Adventure Game
by Gerrit Ohrner
''')

#import os
#filePath = os.path.dirname(os.path.abspath(__file__))
#with open(filePath + '\\Test.txt', "r") as f:
#	content = f.readlines()
#print(content)

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
	if Winput != 0:
		for Winput <= len(content_walls)
			print(content_walls[Winput])
			Winput++
			break
	else:
		print(content_walls[0])
	#content_walls
	#Mehrere texte, wenn man die Waende beruehrt
	#irgendwann laesst man den spieler genervt auf der anderen Seite erscheinen. 
	#counter reseten, wenn man nicht mehr gegen eine Wand läuft

	input()
	return

def wrong_input():
	#content_input
	input()
	#jedes mal, wenn man keine Richtung eingibt (north, east, south, west), wird ein 
	#Zaehler incrementiert und aufeinander folgende Texte werden ausgegeben.
	
while direction != "exit":
	rooms(rcounter)
	direction = input('In which direction do you want to move?(north/east/south/west)')
	rcounterBackup = rcounter
	if direction == "north":
		rcounter = rcounter + 3
	elif direction == 'east':
		if rcounter == 3 or rcounter == 6:
			rcounter = rcounterBackup
			hittin_walls()
		else:
			rcounter = rcounter + 1
	elif direction == 'south':
		rcounter = rcounter - 3
	elif direction == 'west':
		if rcounter == 4 or rcounter == 7:
			rcounter = rcounterBackup
			hittin_walls()
		else:
			rcounter = rcounter - 1
	else:
		wrong_input()
	
	if rcounter < 1:
		rcounter = rcounterBackup
		hittin_walls()
	elif rcounter > 9:
		rcounter = rcounterBackup
		hittin_walls()
	input()
	os.system('cls' if os.name == 'nt' else 'clear')
