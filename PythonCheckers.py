BLUE = '\033[94m'
RED = '\033[91m'
END = '\033[0m'
counterstaken = 0
import copy
import time
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
class EnemyKing(object):
    def __repr__(self):
        return EnemyKing()
    def __str__(self):
        return RED + "|King   |" + END
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

class Moves:
       
    def __init__(self, startpos, endpos):
        self.startpos = startpos
        self.endpos = endpos

        #def doMove(self, board):
        #	return board;

        #def undoMove(self, board):
        #	return board;
replaylist = []
movelist = []
redolist = []
player2movelist = []
player2redolist = []
Enemy = EnemyCounter()
secondturn = 0

board =[["      ","   1   ", "     2    ","    3    ","    4    ","   5   ", "      6   ","    7    ","    8    "], 
             ["   1 ", EmptySpace(), EmptySpace(),EmptySpace(),EnemyCounter() , EmptySpace(), EnemyCounter(),EmptySpace(), EnemyCounter()], 
             ["   2 " , FriendlyCounter(), EmptySpace(),EmptySpace(), EmptySpace(), EnemyCounter(), EmptySpace(),EnemyCounter(), EmptySpace()],
             ["   3 " , EmptySpace(), EmptySpace(),EmptySpace(), EnemyCounter(), EmptySpace(), EnemyCounter(),EmptySpace(), EnemyCounter()],
             ["   4 " , EmptySpace(),EmptySpace(),FriendlyCounter(), EmptySpace(),EmptySpace(),EmptySpace(), FriendlyCounter(), EmptySpace()],
             ["   5 " , EmptySpace(),EmptySpace(), EmptySpace(), EnemyCounter(),EmptySpace(),EnemyKing(), EmptySpace(), EmptySpace()],
             ["   6 " , FriendlyCounter(), EmptySpace(),FriendlyCounter(), EmptySpace(), FriendlyCounter(), EmptySpace(),FriendlyCounter(), EmptySpace()],
             ["   7 " , EmptySpace(), FriendlyCounter(),EmptySpace(), FriendlyCounter(), EmptySpace(), FriendlyCounter(),EmptySpace(), EnemyCounter()], 
             ["   8 ", FriendlyCounter(), EmptySpace(),FriendlyCounter(), EmptySpace(), FriendlyCounter(), EmptySpace(),EmptySpace(), EmptySpace()]]

a = [(ix,iy,type(i)) for ix, row in enumerate(board) for iy, i in enumerate(row) if type(i) == type(Enemy)]
player2counterstaken = 0
aicounterstaken = 0
print "if you see this more than once, shits broken"
replayboard = copy.deepcopy(board)
turn = ""
player = ""
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
def userturnlogic(secondturn, player, turn, counterstaken, board, player2counterstaken):
    if player == "1":
        counter = FriendlyCounter()
        ecounter = EnemyCounter()
        ctaken = counterstaken
        print "Player 1's turn"
        turn = "Player 1"
        king = FriendlyKing()
        eking = EnemyKing()
        colour = BLUE
    elif player == "2":
        counter = EnemyCounter()
        ecounter = FriendlyCounter()
        ctaken = player2counterstaken
        king = EnemyKing()
        eking = FriendlyKing()
        print "Player 2's turn"
        turn = "Player 2"
        colour = RED

    print counterstaken
    print "f"
    print secondturn
    valid = 0
    undoboard = copy.deepcopy(board)
    while True:
        if secondturn == 0:
            while True:
                counter_to_move_input = raw_input(colour + "Enter the row number of the counter you wish to move: " + END)
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
                counter_to_movey_input = raw_input(colour + "Enter the column number of the counter you wish to move: " + END)
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

            if type(board[counter_to_move][counter_to_movey]) == type(EmptySpace()):
                print"There is no counter in this position "
                continue
            if type(board[counter_to_move][counter_to_movey]) == type(ecounter) or type(board[counter_to_move][counter_to_movey]) == type(eking):
                print"That is an enemy counter"
                continue
            else:
                break
        else:
            counter_to_move = "1"
            counter_to_movey = "2"
            break
    valid_move = 0;
    while valid_move == 0:
        #try:
        while True:
            counter_to_move_to_input = raw_input(colour + "Enter the row number of the counter you wish to move to: " + END)
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
            counter_to_move_toy_input = raw_input(colour + "Enter the column number of the counter you wish to move to: " + END)
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
        if type(board[counter_to_moveto][counter_to_movetoy]) == type(counter) or type(board[counter_to_moveto][counter_to_movetoy]) == type(eking) or type(board[counter_to_moveto][counter_to_movetoy]) == type(king) or type(board[counter_to_moveto][counter_to_movetoy]) == type(ecounter):
            print"There is already a counter in this position"
            continue
        #if board[counter_to_move-1][counter_to_movey+1] == Enemy or board[counter_to_move-1][counter_to_movey-1] == Enemy:
            #if board[counter_to_move-2][counter_to_movey+2] != counter or board[counter_to_move-2][counter_to_movey-2] != counter:
                #if displacement not in [(2,2), (2,-2)]: 
                    #print "Not a valid move, you must take the available enemy counter"
                    #continue 
        if type(board[counter_to_move][counter_to_movey]) == type(counter):
            if displacement == (2,-2):
                    print "00000"
                    if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                        board[counter_to_moveto+1][counter_to_movetoy-1] = EmptySpace()
                        board[counter_to_move][counter_to_movey] = EmptySpace()
                        board[counter_to_moveto][counter_to_movetoy] = counter
                        ctaken = ctaken + 1
                        valid_move = 1;
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                        print "counters taken =: " ,ctaken
                        secondturn = "1"
                        userturnlogic(secondturn, player, turn, counterstaken, board, player2counterstaken)
                    elif board[counter_to_moveto+1][counter_to_movetoy-1] != counter:
                        print "Not a valid move-"
                        print board[counter_to_moveto+1][counter_to_movetoy-1]
                        continue
            if displacement == (2,2):
                if type(board[counter_to_moveto+1][counter_to_movetoy+1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or  type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking) or board[counter_to_moveto+1][counter_to_movetoy+1] == EmptySpace():
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto][counter_to_movetoy] = counter
                    ctaken = ctaken + 1
                    valid_move = 1;    
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                    print "counters taken =: " ,ctaken
            if displacement == (-2,-2):
                    if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                        board[counter_to_moveto-1][counter_to_movetoy-1] = EmptySpace()
                        board[counter_to_move][counter_to_movey] = EmptySpace()
                        board[counter_to_moveto][counter_to_movetoy] = counter
                        ctaken = ctaken + 1
                        valid_move = 1;
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                        print "counters taken =: " ,ctaken
                        #userturnlogic(secondturn, player, turn, counterstaken, board, player2counterstaken)
                    elif board[counter_to_moveto+1][counter_to_movetoy-1] != counter:
                        print "Not a valid move-"
                        print board[counter_to_moveto+1][counter_to_movetoy-1]
                        continue
            if displacement == (-2,2):
                if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                    board[counter_to_moveto-1][counter_to_movetoy+1] = EmptySpace()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto][counter_to_movetoy] = counter
                    caken = ctaken + 1
                    valid_move = 1;    
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                    print "counters taken =: " ,ctaken
                    #userturnlogic(secondturn, player, turn, counterstaken, board, player2counterstaken)
                elif board[counter_to_moveto+1][counter_to_movetoy-1] != ecounter:
                    print "Not a valid move--"
                    continue
        elif type(board[counter_to_move][counter_to_movey]) == type(king):
            if displacement == (2,-2):
                    if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                        board[counter_to_moveto+1][counter_to_movetoy-1] = EmptySpace()
                        board[counter_to_move][counter_to_movey] = EmptySpace()
                        board[counter_to_moveto][counter_to_movetoy] = king
                        ctaken = ctaken + 1
                        valid_move = 1;
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                        print "counters taken =: " ,ctaken
                        #userturnlogic(secondturn, player, turn, counterstaken, board, player2counterstaken)
                    elif board[counter_to_moveto+1][counter_to_movetoy-1] != counter:
                        print "Not a valid move-"
                        print board[counter_to_moveto+1][counter_to_movetoy-1]
                        continue
            if displacement == (2,2):
                if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                    board[counter_to_moveto+1][counter_to_movetoy+1] = EmptySpace()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto][counter_to_movetoy] = king
                    ctaken = ctaken + 1
                    valid_move = 1;    
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                    print "counters taken =: " ,ctaken
            if displacement == (-2,-2):
                    if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                        board[counter_to_moveto-1][counter_to_movetoy-1] = EmptySpace()
                        board[counter_to_move][counter_to_movey] = EmptySpace()
                        board[counter_to_moveto][counter_to_movetoy] = king
                        ctaken = ctaken + 1
                        valid_move = 1;
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                        print "counters taken =: " ,ctaken
                        #userturnlogic(secondturn, player, turn, counterstaken, board, player2counterstaken)
                    elif board[counter_to_moveto+1][counter_to_movetoy-1] != counter:
                        print "Not a valid move-"
                        print board[counter_to_moveto+1][counter_to_movetoy-1]
                        continue
            if displacement == (-2,2):
                if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                    board[counter_to_moveto-1][counter_to_movetoy+1] = EmptySpace()
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_moveto][counter_to_movetoy] = counter
                    caken = ctaken + 1
                    valid_move = 1;    
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                    print "counters taken =: " ,ctaken
                    #userturnlogic(secondturn, player, turn, counterstaken, board, player2counterstaken)
                elif board[counter_to_moveto+1][counter_to_movetoy-1] != ecounter:
                    print "Not a valid move--"
                    continue
        if player == "1":
            if board[counter_to_moveto+1][counter_to_movetoy-1] == counter:
                if counter_to_moveto is counter_to_move - 2 or counter_to_movetoy is counter_to_movey - 2  :
                    print"Not a valid move---"
                    continue
        if counter_to_moveto == counter_to_move - 1 and counter_to_movetoy == counter_to_movey:
            print "Not a valid move----"
            continue
        #elif counter_to_moveto is not counter_to_move - 1 or counter_to_movetoy is  counter_to_movey  :
        #    print"Not a valid move"
        if player == "1":
            if type(board[counter_to_move][counter_to_movey]) == type(counter):
                if counter_to_move != counter_to_moveto +1: 
                    print "Not a valid move, blue counters can only move up the board" 
                    continue
        elif player == "2":
            if type(board[counter_to_move][counter_to_movey]) == type(counter):
                if counter_to_move != counter_to_moveto -1: 
                    print"Not a valid move red counters can only move down the board" 
                    continue
        else:
            if counter_to_move != counter_to_moveto -1:
                print "Not a valid move="
        if board[counter_to_moveto][counter_to_movetoy] == "      " or board[counter_to_moveto][counter_to_movetoy] == "   1   " or board[counter_to_moveto][counter_to_movetoy] == "     2    " or board[counter_to_moveto][counter_to_movetoy] == "    3    " or board[counter_to_moveto][counter_to_movetoy] == "    4    " or board[counter_to_moveto][counter_to_movetoy] == "   5   " or board[counter_to_moveto][counter_to_movetoy] == "      6   " or board[counter_to_moveto][counter_to_movetoy] == "    7    " or board[counter_to_moveto][counter_to_movetoy] == "    8    ":
            print"Not a valid position" 
            continue
        else:
            if type(board[counter_to_move][counter_to_movey]) == type(king):
                board[counter_to_move][counter_to_movey] = EmptySpace()
                board[counter_to_moveto][counter_to_movetoy] = king
                valid_move = 1
                print "nf"
                print king
            else:
                valid_move = 1
                board[counter_to_move][counter_to_movey] = EmptySpace()
                board[counter_to_moveto][counter_to_movetoy] = counter
                #counterstaken = counterstaken + 1
    reversedisplacement = (displacement[0], displacement[1])
    if player == "1":
        if counter_to_moveto == 1:
            board[counter_to_moveto][counter_to_movetoy] = king
    elif player == "2":
        if counter_to_moveto == 8:
            board[counter_to_moveto][counter_to_movetoy] = king
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in board]))
    print "counters taken =: " ,ctaken
    undofuncion(counterstaken, player2counterstaken, replaylist, turn, board,counter_to_move,counter_to_movey, counter_to_moveto,counter_to_movetoy, movelist, redolist)
   


def undofuncion(counterstaken, player2counterstaken, replaylist, turn, board,counter_to_move,counter_to_movey, counter_to_moveto,counter_to_movetoy, movelist, redolist):
    if turn == "Player 1":
        mlist = movelist
        rlist = player2redolist
        counter = FriendlyCounter()
        ctaken = counterstaken
    else:
        mlist = player2movelist
        rlist = player2redolist
        counter = EnemyCounter()
        ctaken = player2counterstaken
    startposx = counter_to_move
    startposy = counter_to_movey
    endposx = counter_to_moveto 
    endposy = counter_to_movetoy 
    startpos = (startposx, startposy)
    endpos = (endposx, endposy)
    move = (startpos, endpos)
    mlist.insert(0,move)
    replaylist.append(move)
    print "1"
    print movelist
    print "2"
    print player2movelist
    while True:
        if mlist:
            undoa = raw_input("Undo move? Y/N: ")
            if undoa in ['y', 'Y']:
                    for i in mlist:
                        print i
                        endpos1 = i[0]
                        startpos1 = i[1]
                        xt,yt = endpos1
                        x,y = startpos1
                        a = startpos1 
                        b = endpos1
                        displacement = (startpos1[0] - endpos1[0], startpos1[1] - endpos1[1])
                        if displacement == (2,-2):
                            board[x-1][y+1] = counter
                        elif displacement == (2,2):
                            board[x-1][y-1] = counter
                        board[xt][yt] = counter
                        board[x][y] = EmptySpace()
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                                for row in board]))
                        print "counters taken =: " ,ctaken
                        rlist.append(i)
                        mlist.remove(i)
                        continue
            elif undoa == 'r':
                replay(replayboard, replaylist)
            else:
                break
            if rlist:
                redomove = raw_input("Redo Y/N: ")
                if redomove in ['y', 'Y']:
                    for i in rlist:
                        print i
                        startpos1 = i[0]
                        endpos1 = i[1]
                        xt,yt = startpos1
                        x,y = endpos1
                        a = endpos1 
                        b = startpos1
                        displacement = (startpos1[0] - endpos1[0], startpos1[1] - endpos1[1])
                        if displacement == (2,-2):
                            board[x-1][y+1] = counter
                        elif displacement == (2,2):
                            board[x-1][y-1] = counter
                        board[xt][yt] = EmptySpace()
                        board[x][y] = counter
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                                for row in board]))
                        print "counters taken =: " ,ctaken
                        rlist.remove(i)
                        continue
            else:
                break
        else:
            break
def AIturnlogic(board, aicounterstaken):
    a = [(ix,iy,type(i)) for ix, row in enumerate(board) for iy, i in enumerate(row) if type(i) == type(Enemy)]    
    c = str(a[1])
    x = int(c[-38])
    y = int(c[-35])
    print x,y
def replay(replayboard, replaylist):
    print replaylist
    replay = raw_input("Press P to begin the replay: ")
    if replay in ['p', 'P']:
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in replayboard]))
        for i in replaylist:
                        startpos1 = i[0]
                        endpos1 = i[1]
                        xt,yt = startpos1
                        x,y = endpos1
                        a = endpos1 
                        b = startpos1
                        displacement = (startpos1[0] - endpos1[0], startpos1[1] - endpos1[1])
                        if displacement == (2,-2):
                            replayboard[x-1][y+1] = EnemyCounter()
                        elif displacement == (2,2):
                            replayboard[x-1][y-1] = EnemyCounter()
                        replayboard[xt][yt] = EmptySpace()
                        replayboard[x][y] = FriendlyCounter()
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                                for row in replayboard]))
                        replaylist.remove(i)
                        time.sleep(5)
                        continue
def youwin():
    text = [["|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | ||  |"], 
            ["|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| ||  |"], 
            ["|       ||  | |  ||  |_|  |  |       ||   | |       ||  |"], 
            ["|_     _||  |_|  ||       |  |       ||   | |  _    ||__| "],
            ["  |   |  |       ||       |  |   _   ||   | | | |   | __  "],
            ["  |___|  |_______||_______|  |__| |__||___| |_|  |__||__|"]]

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in text]))
def youlose():
    textl = [["|  | |  ||       ||  | |  |  |   |    |       ||       ||       |  |   |  |    |"], 
             ["|  |_|  ||   _   ||  | |  |  |   |    |   _   ||  _____||    ___|  |___| |    _|"], 
             ["|       ||  | |  ||  |_|  |  |   |    |  | |  || |_____ |   |___    ___  |   |"],   
             ["|_     _||  |_|  ||       |  |   |___ |  |_|  ||_____  ||    ___|  |   | |   |"],   
               ["|   |  |       ||       |  |       ||       | _____| ||   |___   |___| |   |_"],  
               ["|___|  |_______||_______|  |_______||_______||_______||_______|         |____|"]]
      
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in textl]))
def Player1(player):
        player = "1"
        userturnlogic(secondturn, player, turn, counterstaken, board, player2counterstaken)

def Player2(player):
        player = "2"
        userturnlogic(secondturn, player, turn, counterstaken, board, player2counterstaken)

print("Alistair Mckay")
print("40207511")
print("Algorithms & Data Structures Coursework")
print("Enter co-ordinates of counter in the form (vertical,horizontal)")
undo_no = ""
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
        while True:
            Player1(player)
            Player2(player)
            print "j"
            print counterstaken
        youwin()
    elif begin == '2':
        print "AI"
        
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in board]))
        print "counters taken =: " ,counterstaken
            
    while counterstaken == 0:
        Player1(player)
        AIturnlogic(board, aicounterstaken)
        print counterstaken
    youwin()