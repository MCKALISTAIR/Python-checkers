BLUE = '\033[94m'
RED = '\033[91m'
END = '\033[0m'
counterstaken = 0
import copy

class FriendlyCounter(object):
    def __repr__(self):
        return FriendlyCounter()
    def __str__(self):
        return BLUE + "|Counter|" + END
class FriendlyKing(object):
    def __repr__(self):
        return FriendlyKing()
    def __str__(self):
        return BLUE + "|King   |" + END
class EnemyCounter(object):
    def __init__(self):
        self.type = 'enemy'
    def __repr__(self):
        return EnemyCounter()
    def __str__(self):
        return RED + "|Counter|" + END
class EmptySpace(object):
    def __repr__(self):
        return EmptySpace()
    def __str__(self):
        return "|       |"


#class Moves(startpos, endpos):
        #def __init__(self, startpos, endpos):
            #self.startpos = startpos
            #self.endpos = endpos

        #def doMove(self, board):
        #	return board;

        #def undoMove(self, board):
        #	return board;

#create seperate instances of each counter
#save start and end  pos
#add to a list each move
#board[counter_to_move][counter_to_movey] = startposition
#board[counter_to_moveto][counter_to_movetoy] = endposition

movelist = []
Enemy = EnemyCounter()
def checkerboard(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append((i+j) % 2)
    #return board
#for board in checkerboard(8):
    #print(board)

#[Square("empty"), Square('blue'), Square('blueKing')]


board =[["      ","   1   ", "     2    ","    3    ","    4    ","   5   ", "      6   ","    7    ","    8    "], 
             ["   1 ", EmptySpace(), EmptySpace(),EmptySpace(),EnemyCounter() , EmptySpace(), EnemyCounter(),EmptySpace(), EnemyCounter()], 
             ["   2 " , FriendlyCounter(), EmptySpace(),EnemyCounter(), EmptySpace(), EnemyCounter(), EmptySpace(),EnemyCounter(), EmptySpace()],
             ["   3 " , EmptySpace(), EmptySpace(),EmptySpace(), EnemyCounter(), EmptySpace(), EnemyCounter(),EmptySpace(), EnemyCounter()],
             ["   4 " , EmptySpace(),EmptySpace(),FriendlyCounter(), EmptySpace(),EmptySpace(),EmptySpace(), EmptySpace(), EmptySpace()],
             ["   5 " , EmptySpace(),EnemyCounter(),EmptySpace(), EnemyCounter(),EmptySpace(),EmptySpace(), EmptySpace(), EmptySpace()],
             ["   6 " , FriendlyCounter(), EmptySpace(),FriendlyCounter(), EmptySpace(), FriendlyCounter(), EmptySpace(),FriendlyCounter(), EmptySpace()],
             ["   7 " , EmptySpace(), FriendlyCounter(),EmptySpace(), FriendlyCounter(), EmptySpace(), FriendlyCounter(),EmptySpace(), FriendlyCounter()], 
             ["   8 ", FriendlyCounter(), EmptySpace(),FriendlyCounter(), EmptySpace(), FriendlyCounter(), EmptySpace(),FriendlyCounter(), EmptySpace()]]

a = [(ix,iy,type(i)) for ix, row in enumerate(board) for iy, i in enumerate(row) if type(i) == type(Enemy)]
print(type(Enemy))
c = str(a[1])
x = int(c[-38])
y = int(c[-35])
def tutorial():
    tutorialboard = [["      ","   1   ", "     2    ","    3    "],
                    ["   1 ", EmptySpace(), EmptySpace(),EmptySpace(),],
                    ["   2 " , EmptySpace(), EmptySpace(),EnemyCounter(),],
                    ["   3 " , EmptySpace(), EmptySpace(),EmptySpace()]]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in tutorialboard]))
    print"To select this counter you would enter 2 for the row number"
    print"and 3 for the column number"
def userturnlogic(counterstaken, board):
    print "Player 1's turn"
    valid = 0
    undoboard = copy.deepcopy(board)
    while True:
        #try:
        while True:
            counter_to_move_input = raw_input("Enter the row number of the counter you wish to move: ")
            try:
                number = int(counter_to_move_input)
            except ValueError:
                print "Please enter a row number"
                continue
            except SyntaxError:
                print "Please enter a row number"
                continue
            else:
                counter_to_move = int(counter_to_move_input)
                break
        while True:
            counter_to_movey_input = raw_input("Enter the column number of the counter you wish to move: ")
            try:
                numbery = int(counter_to_movey_input)
            except ValueError:
                print "Please enter a column number"
                continue
            except SyntaxError:
                print "Please enter a column number"
                continue
            else:
                counter_to_movey = int(counter_to_movey_input)
                break
         #except:
             #print("Please enter an integer value and not a string")
             #continue

        if type(board[counter_to_move][counter_to_movey]) == type(EmptySpace()):
            print"There is no counter in this position "
            continue
        if type(board[counter_to_move][counter_to_movey]) == type(EnemyCounter()):
            print"That is an enemy counter"
            continue
        else:
            break
    valid_move = 0;
    while valid_move == 0:
        #try:
        while True:
            counter_to_move_to_input = raw_input("Enter the row number of the counter you wish to move to: ")
            try:
                number2 = int(counter_to_move_to_input)
            except ValueError:
                print "Error"
                continue
            except SyntaxError:
                print "Please enter a column number"
                continue
            else:
                counter_to_moveto = int(counter_to_move_to_input)
                break
        while True:
            counter_to_move_toy_input = raw_input("Enter the column number of the counter you wish to move to: ")
            try:
                number3 = int(counter_to_move_toy_input)
            except ValueError:
                print "Error"
                continue
            except SyntaxError:
                print "Please enter a column number"
                continue
            else:
                counter_to_movetoy = int(counter_to_move_toy_input)
                break
        a = (counter_to_move,counter_to_movey) 
        b = (counter_to_moveto,counter_to_movetoy)
        displacement = (a[0] - b[0], a[1] - b[1])
        print displacement        
        if type(board[counter_to_moveto][counter_to_movetoy]) == type(FriendlyCounter()) or type(board[counter_to_moveto][counter_to_movetoy]) == type(EnemyCounter()):
            print"There is already a counter in this position"
            continue
        if board[counter_to_move-1][counter_to_movey+1] == Enemy or board[counter_to_move-1][counter_to_movey-1] == Enemy:
            if board[counter_to_move-2][counter_to_movey+2] != FriendlyCounter() or board[counter_to_move-2][counter_to_movey-2] != FriendlyCounter():
                if displacement not in [(2,2), (2,-2)]: 
                    print "Not a valid move, you must take the available enemy counter"
                    continue 
        if displacement == (2,-2):
                if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(EnemyCounter()):
                    board[counter_to_moveto+1][counter_to_movetoy-1] = EmptySpace()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
                    counterstaken = counterstaken + 1
                    valid_move = 1;
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                    print "counters taken =: " ,counterstaken
                    secondturn(board, counter_to_move, counter_to_moveto, counter_to_movey, counter_to_movetoy, counterstaken)
                elif board[counter_to_moveto+1][counter_to_movetoy-1] != EnemyCounter():
                    print "Not a valid move-"
                    print board[counter_to_moveto+1][counter_to_movetoy-1]
                    continue
        if displacement == (2,2):
            if type(board[counter_to_moveto+1][counter_to_movetoy+1]) == type(EnemyCounter()):
                board[counter_to_moveto+1][counter_to_movetoy+1] = EmptySpace()
                board[counter_to_move][counter_to_movey] = EmptySpace()
                board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
                counterstaken = counterstaken + 1
                valid_move = 1;    
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                  for row in board]))
                print "counters taken =: " ,counterstaken
                secondturn(board, counter_to_move, counter_to_moveto, counter_to_movey, counter_to_movetoy, counterstaken)
            elif board[counter_to_moveto+1][counter_to_movetoy+1] != EnemyCounter():
                print "Not a valid move--"
                continue
        if board[counter_to_moveto+1][counter_to_movetoy-1] == EnemyCounter():
            if counter_to_moveto is counter_to_move - 2 or counter_to_movetoy is counter_to_movey - 2  :
                print"Not a valid move---"
                continue
        if counter_to_moveto == counter_to_move - 1 and counter_to_movetoy == counter_to_movey:
            print "Not a valid move----"
            continue
        #elif counter_to_moveto is not counter_to_move - 1 or counter_to_movetoy is  counter_to_movey  :
        #    print"Not a valid move"
        if board[counter_to_moveto][counter_to_movetoy] == "      " or board[counter_to_moveto][counter_to_movetoy] == "   1   " or board[counter_to_moveto][counter_to_movetoy] == "     2    " or board[counter_to_moveto][counter_to_movetoy] == "    3    " or board[counter_to_moveto][counter_to_movetoy] == "    4    " or board[counter_to_moveto][counter_to_movetoy] == "   5   " or board[counter_to_moveto][counter_to_movetoy] == "      6   " or board[counter_to_moveto][counter_to_movetoy] == "    7    " or board[counter_to_moveto][counter_to_movetoy] == "    8    ":
            print"Not a valid move-----" 
            continue
        if counter_to_move != counter_to_moveto +1: 
            print"Not a valid move------" 
            continue
        else:
            valid_move = 1;
            board[counter_to_move][counter_to_movey] = EmptySpace()
            board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
            #counterstaken = counterstaken + 1
    reversedisplacement = (displacement[0], displacement[1])
    if counter_to_moveto == 1:
        board[counter_to_moveto][counter_to_movetoy] = FriendlyKing()

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in board]))
    print "counters taken =: " ,counterstaken
    startposx = counter_to_move
    startposy = counter_to_movey
    endposx = counter_to_moveto 
    endposy = counter_to_movetoy 
    startpos = (startposx, startposy)
    endpos = (endposx, endposy)
    stuff = (startpos, endpos)
    #movelist.append(startpos, endpos)
    movelist.append(stuff)
    reversedlist = list(reversed(movelist))
    print reversedlist
    for i in reversedlist:
    	dave = i[0]
    	davey = i[1]
    	xt,yt = davey
    	x,y = dave
    print "h"
    board[xt][yt] = EmptySpace()
    board[x][y] = FriendlyCounter()
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in board]))
    while True:
        undo = raw_input("Undo? Y/N: ")
        if undo in ['y', 'Y']:
            undo_no = "no"
            if displacement == (2, -2):
                board[counter_to_move][counter_to_movey] = FriendlyCounter()
                board[counter_to_moveto][counter_to_movetoy] = EmptySpace()
                board[counter_to_moveto+1][counter_to_movetoy-1] = EnemyCounter()
                counterstaken = counterstaken - 1 
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                print "counters taken =: " ,counterstaken
                break
            elif displacement == (2, 2):
                board[counter_to_moveto][counter_to_movetoy] = EmptySpace()
                board[counter_to_move][counter_to_movey] = FriendlyCounter()
                board[counter_to_moveto + 1][counter_to_movetoy +1 ] = EnemyCounter()
                counterstaken = counterstaken - 1
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                print "counters taken =: " ,counterstaken
                break
            else:
                board[counter_to_move][counter_to_movey] = FriendlyCounter()
                board[counter_to_moveto][counter_to_movetoy] = "|       |"
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                print "counters taken =: " ,counterstaken
                break
        elif undo not  in ['y', 'Y', 'n', 'N']:
            print "Please enter Y or N only"
            continue
        else:
            undo_no = "yes"
            break
    print displacement
    if undo_no is not "yes":
        while True:        
            redo = raw_input("Re-do? Y/N: ")
            redo_up = redo.upper()
            if redo_up in ['y', 'Y']:
                if displacement == (2, -2):
                    board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto + 1][counter_to_movetoy -1] = EmptySpace()
                    counterstaken = counterstaken + 1
                    print "jgf"
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                    print "counters taken =: " ,counterstaken
                    break
                elif displacement == (2, 2):
                    board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto + 1][counter_to_movetoy +1] = EmptySpace()
                    counterstaken = counterstaken + 1
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                    print "counters taken =: " ,counterstaken
                    break
                else:
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                    print "counters taken =: " ,counterstaken
                    break
            elif redo_up not  in ['y', 'Y', 'n', 'N']:
                print "Please enter Y or N only"
                continue
            else:
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                     for row in board]))
                print "counters taken =: " ,counterstaken
                break

def player2turnlogic(board, player2counterstaken):
    print RED + "Player 2's turn " + END
    valid = 0
    while True:
        while True:
            counter_to_move_input = raw_input(RED + "Enter the row number of the counter you wish to move: "+ END)
            try:
                number = int(counter_to_move_input)
            except ValueError:
                print RED + "Please enter a row number" + END
                continue
            except SyntaxError:
                print RED + "Please enter a row number" + END
                continue
            else:
                counter_to_move = int(counter_to_move_input)
                break
        while True:
            counter_to_movey_input = raw_input(RED + "Enter the column number of the counter you wish to move: " + END)
            try:
                numbery = int(counter_to_movey_input)
            except ValueError:
                print RED + "Please enter a column number" + END
                continue
            except SyntaxError:
                print RED + "Please enter a column number" + END
                continue
            else:
                counter_to_movey = int(counter_to_movey_input)
                break
        if board[counter_to_move][counter_to_movey] == EmptySpace():
            print RED + "There is no counter in this position " + END
            continue
        if board[counter_to_move][counter_to_movey] == FriendlyCounter():
            print RED + "That is an enemy counter" + END
            continue
        else:
            break
    valid_move = 0;
    while valid_move == 0:
        #try:
        while True:
            counter_to_move_to_input = raw_input("Enter the row number of the counter you wish to move to: ")
            try:
                number2 = int(counter_to_move_to_input)
            except ValueError:
                print "Error"
                continue
            except SyntaxError:
                print "Please enter a column number"
                continue
            else:
                counter_to_moveto = int(counter_to_move_to_input)
                break
        while True:
            counter_to_move_toy_input = raw_input("Enter the column number of the counter you wish to move to: ")
            try:
                number3 = int(counter_to_move_toy_input)
            except ValueError:
                print "Error"
                continue
            except SyntaxError:
                print "Please enter a column number"
                continue
            else:
                counter_to_movetoy = int(counter_to_move_toy_input)
                break
        print board[counter_to_move][counter_to_movey]
        a = (counter_to_move,counter_to_movey) 
        b = (counter_to_moveto,counter_to_movetoy)
        displacement = (a[0] - b[0], a[1] - b[1])
        #if board[counter_to_move][counter_to_movey] == (BLUE + "|King   |" + END):
             #kinglogic()
             #valid_move = 11    1,4 - 3,2 -2,2   1,4 3,6 -2-2
        print board[counter_to_move+1][counter_to_movey+1]
        if type(board[counter_to_move+1][counter_to_movey+1]) == type(FriendlyCounter()) or type(board[counter_to_move+1][counter_to_movey-1]) == type(FriendlyCounter()):
            if displacement not in [(-2,2), (-2,-2)]: 
                print "Not a valid move, you must take the available enemy counter"
                continue 
        if type(board[counter_to_moveto][counter_to_movetoy]) == type(EnemyCounter()) or type(board[counter_to_moveto][counter_to_movetoy]) == type(EnemyCounter()):
            print"There is already a counter in this position"
            continue
        elif displacement == (-2,2):
                if  type(board[counter_to_moveto-1][counter_to_movetoy-1]) == type(FriendlyCounter()):
                    board[counter_to_moveto-1][counter_to_movetoy-1] = EmptySpace()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto][counter_to_movetoy] = EnemyCounter()
                    counterstaken = counterstaken + 1
                    valid_move = 1;
                elif board[counter_to_moveto-1][counter_to_movetoy-1] != FriendlyCounter():
                    print "Not a valid move-"
                    print board[counter_to_moveto-1][counter_to_movetoy-1]
                    continue
        if displacement == (-2,-2):
            if type(board[counter_to_moveto-1][counter_to_movetoy+1]) == type(FriendlyCounter()):
                board[counter_to_moveto-1][counter_to_movetoy+1] = EmptySpace()
                board[counter_to_move][counter_to_movey] = EmptySpace()
                board[counter_to_moveto][counter_to_movetoy] = EnemyCounter()
                player2counterstaken = player2counterstaken + 1
                valid_move = 1;    
            elif board[counter_to_moveto-1][counter_to_movetoy+1] != FriendlyCounter():
                print "Not a valid move--"
                continue
        if type(board[counter_to_moveto-1][counter_to_movetoy-1]) == type(FriendlyCounter()):
            if counter_to_moveto is counter_to_move - 2 or counter_to_movetoy is counter_to_movey - 2  :
                print"Not a valid move---"
                continue
        if counter_to_moveto == counter_to_move + 1 and counter_to_movetoy == counter_to_movey:
            print "Not a valid move----"
            continue
        #elif counter_to_moveto is not counter_to_move - 1 or counter_to_movetoy is  counter_to_movey  :
        #    print"Not a valid move"
        if board[counter_to_moveto][counter_to_movetoy] == "      " or board[counter_to_moveto][counter_to_movetoy] == "   1   " or board[counter_to_moveto][counter_to_movetoy] == "     2    " or board[counter_to_moveto][counter_to_movetoy] == "    3    " or board[counter_to_moveto][counter_to_movetoy] == "    4    " or board[counter_to_moveto][counter_to_movetoy] == "   5   " or board[counter_to_moveto][counter_to_movetoy] == "      6   " or board[counter_to_moveto][counter_to_movetoy] == "    7    " or board[counter_to_moveto][counter_to_movetoy] == "    8    ":
            print"Not a valid move-----" 
            continue
        if counter_to_move != counter_to_moveto -1: 
            print"Not a valid move------" 
            continue
        else:
            valid_move = 1;
            board[counter_to_move][counter_to_movey] = EmptySpace()
            board[counter_to_moveto][counter_to_movetoy] = EnemyCounter()
            #counterstaken = counterstaken + 1
    reversedisplacement = (displacement[0], displacement[1])
    if counter_to_moveto == 1:
        board[counter_to_moveto][counter_to_movetoy] = EnemyKing()

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in board]))
    print RED + "counters taken =: " + END , player2counterstaken

    while True:
        undo = raw_input("Undo? Y/N: ")
        if undo in ['y', 'Y']:
            undo_no = "no"
            if displacement == (-2, 2):
                board[counter_to_move][counter_to_movey] = EnemyCounter()
                board[counter_to_moveto][counter_to_movetoy] = EmptySpace()
                board[counter_to_moveto+1][counter_to_movetoy-1] = FriendlyCounter()
                player2counterstaken = player2counterstaken - 1 
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                print RED + "counters taken =: " + END ,player2counterstaken
                break
            elif displacement == (-2, -2):
                board[counter_to_moveto][counter_to_movetoy] = EmptySpace()
                board[counter_to_move][counter_to_movey] = EnemyCounter()
                board[counter_to_moveto + 1][counter_to_movetoy +1 ] = FriendlyCounter()
                player2counterstaken = player2counterstaken - 1
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                print RED + "counters taken =: " + END ,player2counterstaken
                break
            else:
                board[counter_to_move][counter_to_movey] = EnemyCounter()
                board[counter_to_moveto][counter_to_movetoy] = "|       |"
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                print RED + "counters taken =: " + END ,player2counterstaken
                break
        elif undo not  in ['y', 'Y', 'n', 'N']:
            print "Please enter Y or N only"
            continue
        else:
            undo_no = "yes"
            break
    print displacement
    if undo_no is not "yes":
        while True:        
            redo = raw_input("Re-do? Y/N: ")
            redo_up = redo.upper()
            if redo_up in ['y', 'Y']:
                if displacement == (-2, 2):
                    board[counter_to_moveto][counter_to_movetoy] = EnemyCounter()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto + 1][counter_to_movetoy -1] = EmptySpace()
                    player2counterstaken = player2counterstaken + 1
                    print "jgf"
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                    print RED + "counters taken =: " + END ,player2counterstaken
                    break
                elif displacement == (-2, -2):
                    board[counter_to_moveto][counter_to_movetoy] = EnemyCounter()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto + 1][counter_to_movetoy +1] = EmptySpace()
                    player2counterstaken = player2counterstaken + 1
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                    print RED + "counters taken =: " + END ,player2counterstaken
                    break
                else:
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto][counter_to_movetoy] = EnemyCounter()
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                    print RED + "counters taken =: " + END ,player2counterstaken
                    break
            elif redo_up not  in ['y', 'Y', 'n', 'N']:
                print "Please enter Y or N only"
                continue
            else:
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                     for row in board]))
                print RED + "counters taken =: " + END ,player2counterstaken
                break    
def secondturn(board, counter_to_move, counter_to_moveto, counter_to_movey, counter_to_movetoy, counterstaken):
    print "second turn"
    print counter_to_moveto
    print counter_to_movetoy
    counter_to_move = counter_to_moveto
    counter_to_movey = counter_to_movetoy
    valid_move = 0;
    while valid_move == 0:
        #try:
        if type(board[counter_to_move-1][counter_to_movey+1]) == type(EnemyCounter()) and type(board[counter_to_move-1][counter_to_movey-1]) == type(EnemyCounter()) and type(board[counter_to_move-2][counter_to_movey+2]) == type(EnemyCounter()) and type(board[counter_to_move-2][counter_to_movey-2]) == type(EnemyCounter()):
        	print"h"
        while True:
            counter_to_move_to_input = raw_input("Enter the row number of the counter you wish to move to: ")
            try:
                number2 = int(counter_to_move_to_input)
            except ValueError:
                print "Error"
                continue
            except SyntaxError:
                print "Please enter a column number"
                continue
            else:
                counter_to_moveto = int(counter_to_move_to_input)
                break
        while True:
            counter_to_move_toy_input = raw_input("Enter the column number of the counter you wish to move to: ")
            try:
                number3 = int(counter_to_move_toy_input)
            except ValueError:
                print "Error"
                continue
            except SyntaxError:
                print "Please enter a column number"
                continue
            else:
                counter_to_movetoy = int(counter_to_move_toy_input)
                break
        a = (counter_to_move,counter_to_movey) 
        b = (counter_to_moveto,counter_to_movetoy)
        displacement = (a[0] - b[0], a[1] - b[1])
        #if board[counter_to_move][counter_to_movey] == (BLUE + "|King   |" + END):
             #kinglogic()
             #valid_move = 1
        print displacement
        if type(board[counter_to_move-1][counter_to_movey+1]) == type(EnemyCounter) or type(board[counter_to_move-1][counter_to_movey-1]) == type(EnemyCounter):
            if type(board[counter_to_move-2][counter_to_movey+2]) != type(FriendlyCounter()) or board[counter_to_move-2][counter_to_movey-2] != type(FriendlyCounter()):
                if displacement not in [(2,2), (2,-2)]: 
                    print "Not a valid move, you must take the available enemy counter"
                    continue 
        if displacement == (2,-2):
                if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(EnemyCounter()):
                    board[counter_to_moveto+1][counter_to_movetoy-1] = EmptySpace()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
                    counterstaken = counterstaken + 1
                    valid_move = 1;
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                    print "counters taken =: " ,counterstaken
                    secondturn(board, counter_to_move, counter_to_moveto, counter_to_movey, counter_to_movetoy)
                elif type(board[counter_to_moveto+1][counter_to_movetoy-1]) != type(EnemyCounter()):
                    print "Not a valid move-"
                    print board[counter_to_moveto+1][counter_to_movetoy-1]
                    continue
        if displacement == (2,2):
            if type(board[counter_to_moveto+1][counter_to_movetoy+1]) == type(EnemyCounter()):
                board[counter_to_moveto+1][counter_to_movetoy+1] = EmptySpace()
                board[counter_to_move][counter_to_movey] = EmptySpace()
                board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
                counterstaken = counterstaken + 1
                valid_move = 1;    
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                  for row in board]))
                print "counters taken =: " ,counterstaken
                secondturn(board, counter_to_move, counter_to_moveto, counter_to_movey, counter_to_movetoy)
            elif board[counter_to_moveto+1][counter_to_movetoy+1] != EnemyCounter():
                print "Not a valid move--"
                continue
        if board[counter_to_moveto+1][counter_to_movetoy-1] == EnemyCounter():
            if counter_to_moveto is counter_to_move - 2 or counter_to_movetoy is counter_to_movey - 2  :
                print"Not a valid move---"
                continue
        if counter_to_moveto == counter_to_move - 1 and counter_to_movetoy == counter_to_movey:
            print "Not a valid move----"
            continue
        print board[counter_to_moveto][counter_to_movetoy]
        if board[counter_to_moveto][counter_to_movetoy] == FriendlyCounter() or board[counter_to_moveto][counter_to_movetoy] == Enemy:
            print"There is already a counter in this position"
            continue
        #elif counter_to_moveto is not counter_to_move - 1 or counter_to_movetoy is  counter_to_movey  :
        #    print"Not a valid move"
        if board[counter_to_moveto][counter_to_movetoy] == "      " or board[counter_to_moveto][counter_to_movetoy] == "   1   " or board[counter_to_moveto][counter_to_movetoy] == "     2    " or board[counter_to_moveto][counter_to_movetoy] == "    3    " or board[counter_to_moveto][counter_to_movetoy] == "    4    " or board[counter_to_moveto][counter_to_movetoy] == "   5   " or board[counter_to_moveto][counter_to_movetoy] == "      6   " or board[counter_to_moveto][counter_to_movetoy] == "    7    " or board[counter_to_moveto][counter_to_movetoy] == "    8    ":
            print"Not a valid move-----" 
            continue
        if counter_to_move != counter_to_moveto +1: 
            print"Not a valid move------" 
            continue
        else:
            valid_move = 1;
            board[counter_to_move][counter_to_movey] = EmptySpace()
            board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
            #counterstaken = counterstaken + 1
    reversedisplacement = (displacement[0], displacement[1])
    if counter_to_moveto == 1:
        board[counter_to_moveto][counter_to_movetoy] = FriendlyKing()

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in board]))
    print "counters taken =: " ,counterstaken

    while True:
        undo = raw_input("Undo? Y/N: ")
        if undo in ['y', 'Y']:
            undo_no = "no"
            if displacement == (2, -2):
                board[counter_to_move][counter_to_movey] = FriendlyCounter()
                board[counter_to_moveto][counter_to_movetoy] = EmptySpace()
                board[counter_to_moveto+1][counter_to_movetoy-1] = EnemyCounter()
                counterstaken = counterstaken - 1 
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                print "counters taken =: " ,counterstaken
                break
            elif displacement == (2, 2):
                board[counter_to_moveto][counter_to_movetoy] = EmptySpace()
                board[counter_to_move][counter_to_movey] = FriendlyCounter()
                board[counter_to_moveto + 1][counter_to_movetoy +1 ] = EnemyCounter()
                counterstaken = counterstaken - 1
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                print "counters taken =: " ,counterstaken
                break
            else:
                board[counter_to_move][counter_to_movey] = FriendlyCounter()
                board[counter_to_moveto][counter_to_movetoy] = "|       |"
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                print "counters taken =: " ,counterstaken
                break
        elif undo not  in ['y', 'Y', 'n', 'N']:
            print "Please enter Y or N only"
            continue
        else:
            undo_no = "yes"
            break
    print displacement
    if undo_no is not "yes":
        while True:        
            redo = raw_input("Re-do? Y/N: ")
            redo_up = redo.upper()
            if redo_up in ['y', 'Y']:
                if displacement == (2, -2):
                    board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto + 1][counter_to_movetoy -1] = EmptySpace()
                    counterstaken = counterstaken + 1
                    print "jgf"
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                    print "counters taken =: " ,counterstaken
                    break
                elif displacement == (2, 2):
                    board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto + 1][counter_to_movetoy +1] = EmptySpace()
                    counterstaken = counterstaken + 1
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                    print "counters taken =: " ,counterstaken
                    break
                else:
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto][counter_to_movetoy] = FriendlyCounter()
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                    print "counters taken =: " ,counterstaken
                    break
            elif redo_up not  in ['y', 'Y', 'n', 'N']:
                print "Please enter Y or N only"
                continue
            else:
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                     for row in board]))
                print "counters taken =: " ,counterstaken
                break

def kinglogic(counter_to_move, counter_to_movey, counter_to_moveto, counter_to_movetoy):
    board[counter_to_move][counter_to_movey] = EmptySpace()
    board[counter_to_moveto][counter_to_movetoy] = BLUE + "|King   |" + END
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                     for row in board]))
def AIturnlogic(board, aicounterstaken):
    #board.index(EmptySpace())
    indices = [i for i, x in enumerate(board) if x == "    4    "]
    #print board[1][4]
    #print "k"
    #print indices
    #print "AI TURN LOGIC GOES HERE"
    #print any((RED + "|Counter|" + END) in sublist for sublist in board)
    #for record in board:
        #for data in record:
                #if data == (RED + "|Counter|" + END):
                    #print data
        #for rowNo in enumerate(board):
            #print(rowNo)
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
undo_no = ""
player2counterstaken = 0
aicounterstaken = 0
while True:
    
    begin = raw_input("Press 1 to play with against the computer, 2 to play against another person, T for tutorial, N to quit: ")
    if begin  ==  "N":
        sys.exit()
    elif begin  not in ['1', '2', 't', 'T']:
        print"Please enter P, T, or N only"
        continue
    elif begin in ['t', 'T']:
        tutorial()
        continue
    elif begin == '1':
        print"Human"
        
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in board]))
        print "counters taken =: " ,counterstaken
        while counterstaken == 0:
            userturnlogic(counterstaken, board)
            player2turnlogic(board, player2counterstaken)
            print counterstaken
        youwin()
    elif begin == '2':
        print "AI"
        
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in board]))
        print "counters taken =: " ,counterstaken
            

    while counterstaken == 0:
        userturnlogic(counterstaken, board)
        AIturnlogic(board, aicounterstaken)
        print counterstaken
    youwin()