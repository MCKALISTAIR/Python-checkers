BLUE = '\033[94m'
RED = '\033[91m'
END = '\033[0m'
import copy
counterstaken = 0
def userturnlogic(counterstaken):
	valid = 0
	undoboard = copy.deepcopy(board)
	while True:
		counter_to_move = int(input("Enter the row number of the counter you wish to move: "))
		counter_to_movey = int(input("Enter the column number of the counter you wish to move: "))
 		
 		if board[counter_to_move][counter_to_movey] == "|      |":
			print"There is no counter in this position "
			continue
		else:
			break
	board[counter_to_move][counter_to_movey] = "|       |"

	valid_move = 0;
	while valid_move == 0:
		counter_to_moveto = int(input("Enter the row number of the position you wish to move to: "))
		counter_to_movetoy = int(input("Enter the column number of the position you wish to move to : "))
		if board[counter_to_moveto][counter_to_movetoy] == BLUE + "|Counter|" + END or board[counter_to_moveto][counter_to_movetoy] == RED + "|Counter|" + END:
			print"There is already a counter in this position"
		if board[counter_to_moveto+1][counter_to_movetoy-1] == RED + "|Counter|" + END:
			  board[counter_to_moveto+1][counter_to_movetoy-1] = "|       |"
			  counterstaken = counterstaken + 1
			  valid_move = 1;
		elif board[counter_to_moveto+1][counter_to_movetoy+1] == RED + "|Counter|" + END:
			  board[counter_to_moveto+1][counter_to_movetoy+1] = "|       |"
			  counterstaken = counterstaken + 2
			  valid_move = 1;	
		if board[counter_to_moveto+1][counter_to_movetoy-1] == RED + "|Counter|" + END:
			if counter_to_moveto is counter_to_move - 2 or counter_to_movetoy is counter_to_movey - 2  :
				print"Not a valid move"

		#elif counter_to_moveto is not counter_to_move - 1 or counter_to_movetoy is  counter_to_movey  :
		#	print"Not a valid move"
		elif counter_to_moveto == "   1 " or counter_to_moveto == "   2 " or counter_to_moveto == "   3 " or counter_to_moveto == "   4 " or counter_to_moveto == "   5 " or counter_to_moveto == "   6 ":
			print"Not a valid move" 
		else:
			valid_move = 1;
	board[counter_to_moveto][counter_to_movetoy] = BLUE + "|Counter|" + END

	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      	for row in board]))
	print counterstaken
	undo = raw_input("Undo? Y/N: ")
	undo_up = undo.upper()
	if undo_up == "Y":
		print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      		for row in undoboard]))
		redo = raw_input("Re-do? Y/N: ")
		redo_up = redo.upper()
		if redo_up == "Y":
			print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      			for row in board]))
		else:
			print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      			for row in undoboard]))

def AIturnlogic():
	print"AI TURN LOGIC GOES HERE"
def youwin():
	text = [["|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | ||  |"], 
			["|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| ||  |"], 
			["|       ||  | |  ||  |_|  |  |       ||   | |       ||  |"], 
			["|_     _||  |_|  ||       |  |       ||   | |  _    ||__| "],
  			["  |   |  |       ||       |  |   _   ||   | | | |   | __  "],
			["  |___|  |_______||_______|  |__| |__||___| |_|  |__||__|"]]

	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    	for row in text]))
def youloose():
	textl = [["__   __  _______  __   __    ___      _______  _______  _______  _______    ___    ____ "], 
			["|  | |  ||       ||  | |  |  |   |    |       ||       ||       ||       |  |   |  |    | "],
			["|  |_|  ||   _   ||  | |  |  |   |    |   _   ||   _   ||  _____||    ___|  |___| |    _| "],
			["|       ||  | |  ||  |_|  |  |   |    |  | |  ||  | |  || |_____ |   |___    ___  |   |   "],
			["|_     _||  |_|  ||       |  |   |___ |  |_|  ||  |_|  ||_____  ||    ___|  |   | |   |   "],
  			["  |   |  |       ||       |  |       ||       ||       | _____| ||   |___   |___| |   |_  "],
  			["  |___|  |_______||_______|  |_______||_______||_______||_______||_______|         |____|"]]
  	
  	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    	for row in textl]))
  	
print("Alistair Mckay")
print("40207511")
print("Algorithms & Data Structures Coursework")
print("Enter co-ordinates of counter in the form (vertical,horizontal)")

while True:
	
	begin = raw_input("Press Y to begin, N to quit: ")
	if begin  ==  "N":
		sys.exit()
	if begin is not "Y":
		print"Please enter Y or N only"
		continue
	elif begin == "Y":

		board =[["      ","   1   ", "     2    ","    3    ","    4    ","   5   ", "      6   ","    7    ","    8    "], 
		 	["   1 ", "|       |", (RED + "|Counter|" + END),"|       |", (RED + "|Counter|" + END), "|       |", (RED + "|Counter|" + END),"|       |", RED + "|Counter|" + END], 
		 	["   2 " , (RED + "|Counter|" + END), "|       |",(RED + "|Counter|" + END), "|       |", (RED + "|Counter|" + END), "|       |",(RED + "|Counter|" + END), "|       |"],
		 	["   3 " , "|       |", (RED + "|Counter|" + END),"|       |", (RED + "|Counter|" + END), "|       |", (RED + "|Counter|" + END),"|       |", (RED + "|Counter|" + END)],
		 	["   4 " , "|       |","|       |","|       |", "|       |","|       |","|       |", "|       |", "|       |"],
		 	["   5 " , "|       |","|       |","|       |", (RED + "|Counter|" + END),"|       |","|       |", "|       |", "|       |"],
		 	["   6 " , (BLUE + "|Counter|" + END), "|       |",BLUE + "|Counter|" + END, "|       |", BLUE + "|Counter|" + END, "|       |",BLUE + "|Counter|" + END, "|       |"],
		 	["   7 " , "|       |", BLUE + "|Counter|" + END,"|       |", BLUE + "|Counter|" + END, "|       |", BLUE + "|Counter|" + END,"|       |", BLUE + "|Counter|" + END], 
		 	["   8 ", BLUE + "|Counter|" + END, "|       |",BLUE + "|Counter|" + END, "|       |", BLUE + "|Counter|" + END, "|       |",BLUE + "|Counter|" + END, "|       |"]]
		print "counters taken =: " 
		print counterstaken
		print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      	for row in board]))
		
		break	
win = 0
while win == 0:
	userturnlogic(counterstaken)
	AIturnlogic()