import copy
def userturnlogic():
	valid = 0
	while True:
		counter_to_move = int(input("Enter the row number of the counter you wish to move: "))
		counter_to_movey = int(input("Enter the column number of the counter you wish to move: "))
 		
 		if not counter_to_move.isdigit() == False:
 			print "Please enter your desired using the format (row, column)"
 		elif board[counter_to_move][counter_to_movey] == "|      |":
			print"There is no counter in this position"
			continue
		else:
			break
	board[counter_to_move][counter_to_movey] = "|       |"

	valid_move = 0;
	while valid_move == 0:
		counter_to_moveto = int(input("Enter the row number of the position you wish to move to: "))
		counter_to_movetoy = int(input("Enter the column number of the position you wish to move to : "))
		if board[counter_to_moveto][counter_to_movetoy] == "|Counter|":
			print"There is already a counter in this position"
		elif counter_to_moveto is not counter_to_move - 1 or counter_to_movetoy is  counter_to_movey  :
			print"Not a valid move"
		elif counter_to_moveto == "   1 " or counter_to_moveto == "   2 " or counter_to_moveto == "   3 " or counter_to_moveto == "   4 " or counter_to_moveto == "   5 " or counter_to_moveto == "   6 ":
			print"Not a valid move" 
		else:
			valid_move = 1;
	board[counter_to_moveto][counter_to_movetoy] = "|Counter|"

	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      	for row in board]))
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
	textl = [["  __   __  _______  __   __    ___      _______  _______  _______  _______    ___    ____ "], 
			["	|  | |  ||       ||  | |  |  |   |    |       ||       ||       ||       |  |   |  |    | "],
			["  |  |_|  ||   _   ||  | |  |  |   |    |   _   ||   _   ||  _____||    ___|  |___| |    _| "],
			["	|       ||  | |  ||  |_|  |  |   |    |  | |  ||  | |  || |_____ |   |___    ___  |   |   "],
			["	|_     _||  |_|  ||       |  |   |___ |  |_|  ||  |_|  ||_____  ||    ___|  |   | |   |   "],
  			["	  |   |  |       ||       |  |       ||       ||       | _____| ||   |___   |___| |   |_  "],
  			["	  |___|  |_______||_______|  |_______||_______||_______||_______||_______|         |____|"]]

  	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    	for row in textl]))

print("Alistair Mckay")
print("40207511")
print("Algorithms & Data Structures Coursework")
print("Game instructions")
while True:
	
	begin = raw_input("Press Y to begin, N to quit: ")
	if begin  ==  "N":
		sys.exit()
	if begin is not "Y":
		print"Please enter Y or N only"
		continue
	elif begin == "Y":

		board =[["      ","   1   ", "     2    ","    3    ","    4    ","   5   ", "      6   ","    7    ","    8    "], 
		 	["   1 ", "|       |", "|Counter|","|       |", "|Counter|", "|       |", "|Counter|","|       |", "|Counter|"], 
		 	["   2 " , "|Counter|", "|       |","|Counter|", "|       |", "|Counter|", "|       |","|Counter|", "|       |"],
		 	["   3 " , "|       |", "|Counter|","|       |", "|Counter|", "|       |", "|Counter|","|       |", "|Counter|"],
		 	["   4 " , "|       |","|       |","|       |", "|       |","|       |","|       |", "|       |", "|       |"],
		 	["   5 " , "|       |","|       |","|       |", "|       |","|       |","|       |", "|       |", "|       |"],
		 	["   6 " , "|Counter|", "|       |","|Counter|", "|       |", "|Counter|", "|       |","|Counter|", "|       |"],
		 	["   7 " , "|       |", "|Counter|","|       |", "|Counter|", "|       |", "|Counter|","|       |", "|Counter|"], 
		 	["   8 ", "|Counter|", "|       |","|Counter|", "|       |", "|Counter|", "|       |","|Counter|", "|       |"]]
		print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      	for row in board]))
		break	
win = 0
while win == 0:
	userturnlogic()
	AIturnlogic()