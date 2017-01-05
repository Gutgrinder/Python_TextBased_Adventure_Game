print('''
TextBased Adventure Game
by Gerrit Ohrner
''')
import os # os.system('cls' if os.name == 'nt' else 'clear') ///to clear the terminalscreen
os.system('cls' if os.name == 'nt' else 'clear')
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

def hittin_walls(rcounter, rcounterBackup):
#	#Mehrere texte, wenn man die Waende beruehrt
#	#irgendwann laesst man den spieler genervt auf der anderen seite erscheinen. (Well, you are a wizard now. Are you happy?)
	print('You can\'t go this way, there is a Wall.')
	input()
	return rcounter

while direction != "exit":
	rooms(rcounter)
	direction = input('In which direction do you want to move?(north/east/south/west)')
	rcounterBackup = rcounter
	if direction == "north":
		rcounter = rcounter + 3
	elif direction == 'east':
		if rcounter == 3 or rcounter == 6:
			rcounter = rcounterBackup
			hittin_walls(rcounter, rcounterBackup)
		else:
			rcounter = rcounter + 1
	elif direction == 'south':
		rcounter = rcounter - 3
	elif direction == 'west':
		if rcounter == 4 or rcounter == 7:
			hittin_walls(rcounter, rcounterBackup)
			rcounter = rcounterBackup
		else:
			rcounter = rcounter - 1
	else:
		print('Thats not actually a direction, you know?')
		input()
	
	if rcounter < 1:
		rcounter = rcounterBackup
		hittin_walls(rcounter, rcounterBackup)
	elif rcounter > 9:
		rcounter = rcounterBackup
		hittin_walls(rcounter, rcounterBackup)
	input()
	os.system('cls' if os.name == 'nt' else 'clear')
	