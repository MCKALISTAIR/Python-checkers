#Colour variables
BLUE = '\033[94m'
RED = '\033[91m'
END = '\033[0m'
#External functions required for certain operations 
import copy
import time
#Classes for counters, kings, and empty spaces
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
#Lists for undo, replay, stalemate, win and lose
replaylist = []
movelist = []
redolist = []
friendlycounterlist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
enemycounterlist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
player2movelist = []
player2redolist = []
Enemy = EnemyCounter()
secondturn = "0"
#The main game board
board =[["      ","   1   ", "     2    ","    3    ","    4    ","   5   ", "      6   ","    7    ","    8    "], 
             ["   1 ", EmptySpace(), EmptySpace(),EmptySpace(),EmptySpace() , EmptySpace(), EmptySpace(),EmptySpace(), EmptySpace()], 
             ["   2 " , FriendlyCounter(), EmptySpace(),EnemyCounter(), EmptySpace(), EnemyCounter(), EmptySpace(),EmptySpace(), EmptySpace()],
             ["   3 " , EmptySpace(), EmptySpace(),EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(),EmptySpace(), EmptySpace()],
             ["   4 " , EmptySpace(),EnemyCounter(),EmptySpace(), EmptySpace(),EmptySpace(),EmptySpace(), EmptySpace(), EmptySpace()],
             ["   5 " , EmptySpace(),EmptySpace(), EmptySpace(), EmptySpace(),EmptySpace(),EmptySpace(), EmptySpace(), EmptySpace()],
             ["   6 " , EmptySpace(), EmptySpace(),EmptySpace(), EmptySpace(),EmptySpace(), EmptySpace(),EmptySpace(), EmptySpace()],
             ["   7 " , EnemyCounter(), EmptySpace(),FriendlyKing(), EmptySpace(), FriendlyKing(), EmptySpace(),EmptySpace(), EmptySpace()], 
             ["   8 ", EmptySpace(), EmptySpace(),EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(),EmptySpace(), EmptySpace()]]
replayboard = copy.deepcopy(board)
turn = ""
player = ""
#Basic tutorial to explain game modes
def tutorial():
    tutorialboard = [["      ","   1   ", "     2    ","    3    "],
                    ["   1 ", EmptySpace(), EmptySpace(),EmptySpace(),],
                    ["   2 " , EmptySpace(), EmptySpace(),EnemyCounter(),],
                    ["   3 " , EmptySpace(), EmptySpace(),EmptySpace()]]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in tutorialboard]))
    print"To select this counter you would enter 2 for the row number"
    print"and 3 for the column number"
#Main movement function which works with both teams in the same function
def userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board):
    #Variable to only allow one force-jump
    fjump = 0
    #This sets up the function for the blue team
    if player == "1":
        counter = FriendlyCounter()
        ecounter = EnemyCounter()
        counterlist = friendlycounterlist
        print "Player 1's turn"
        turn = "Player 1"
        king = FriendlyKing()
        eking = EnemyKing()
        colour = BLUE
    # This sets up the function for the red team
    elif player == "2":
        counter = EnemyCounter()
        ecounter = FriendlyCounter()
        counterlist = enemycounterlist
        king = EnemyKing()
        eking = FriendlyKing()
        print "Player 2's turn"
        turn = "Player 2"
        colour = RED
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in board]))
    #Keeps the loop open
    valid = 0
    while True:
        #This would be used for the second turn function
        if secondturn == "0":
            #Two while loops for entering, and validating the inputs of the coiunter you want to move
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
                if number >8 or number <1:
                    print "Please enter a number between 1 and 8 "
                    continue
                else:
                    happy = raw_input("Are you happy with your selection? Y/N?: ")
                    if happy in ["N", "n"]:
                        continue
                    elif happy in ["y", "Y"]:
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
                if number >8 or number <1:
                    print "Please enter a number between 1 and 8 "
                    continue
                else:
                    happy = raw_input("Are you happy with your selection? Y/N?: ")
                    if happy in ["N", "n"]:
                        continue
                    elif happy in ["y", "Y"]:
                        counter_to_movey = int(counter_to_movey_input)
                        break
            #These two ensure you do not want to move an empty space and a enemy counter
            if type(board[counter_to_move][counter_to_movey]) == type(ecounter) or type(board[counter_to_move][counter_to_movey]) == type(eking):
                print"That is an enemy counter"
                continue
            if type(board[counter_to_move][counter_to_movey]) == type(EmptySpace()):
                print"There is no counter in this position "
                continue
            #Force jump logic to take a counter if it is possible bassed on the counter you selected
            if type(board[counter_to_move][counter_to_movey]) is not type(EmptySpace()):
                if counter_to_movey is not 8:
                    if counter_to_movey is not 7:
                        if type(board[counter_to_move-1][counter_to_movey+1]) == type(ecounter) or type(board[counter_to_move-1][counter_to_movey+1]) == type(eking):
                            if type(board[counter_to_move-2][counter_to_movey+2]) == type(EmptySpace()):
                                print "Force-jump opertunity detected, excecuting1"
                                fjump = 1
                                if type(board[counter_to_move][counter_to_movey]) == type(king):
                                    board[counter_to_move-2][counter_to_movey+2] = king
                                elif type(board[counter_to_move][counter_to_movey]) == type(counter):
                                    board[counter_to_move-2][counter_to_movey+2] = counter
                                time.sleep(3)
                                board[counter_to_move][counter_to_movey] = EmptySpace()
                                board[counter_to_move-1][counter_to_movey+1] = EmptySpace()
                                if type(board[counter_to_move][counter_to_movey]) == type(counter): 
                                    board[counter_to_move-2][counter_to_movey+2] = counter
                                elif type(board[counter_to_move][counter_to_movey]) == type(king):
                                    board[counter_to_move-2][counter_to_movey+2] = king
                                counter_to_move = counter_to_move-2
                                counter_to_movey = counter_to_movey+2
                                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                                    for row in board]))
                                counterlist.pop(0)
                                stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                                checkwin(friendlycounterlist, enemycounterlist)
                                break
            #Force jump logic to take a counter if it is possible bassed on the counter you selected
            if type(board[counter_to_move-1][counter_to_movey-1]) == type(ecounter) or type(board[counter_to_move-1][counter_to_movey-1]) == type(eking):
                if type(board[counter_to_move-2][counter_to_movey-2]) == type(EmptySpace()):
                    print "Force-jump opertunity detected, excecuting"
                    fjump = 1
                    if type(board[counter_to_move][counter_to_movey]) == type(king):
                                board[counter_to_move-2][counter_to_movey-2] = king
                    elif type(board[counter_to_move][counter_to_movey]) == type(counter):
                                board[counter_to_move-2][counter_to_movey-2] = counter
                    time.sleep(3)
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    board[counter_to_move-1][counter_to_movey-1] = EmptySpace()
                    if type(board[counter_to_move][counter_to_movey]) == type(counter): 
                        board[counter_to_move-2][counter_to_movey+2] = counter
                    elif type(board[counter_to_move][counter_to_movey]) == type(king):
                        board[counter_to_move-2][counter_to_movey+2] = king
                    counter_to_move = counter_to_move-2
                    counter_to_movey = counter_to_movey-2
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                        for row in board]))
                    counterlist.pop(0)
                    stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                    checkwin(friendlycounterlist, enemycounterlist)
                    break
            #Force jump logic to take a counter if it is possible bassed on the counter you selected
            if counter_to_movey is not 8:
                if type(board[counter_to_move][counter_to_movey]) is not type(FriendlyCounter()):
                    if type(board[counter_to_move+1][counter_to_movey+1]) == type(ecounter) or type(board[counter_to_move+1][counter_to_movey+1]) == type(eking):
                        if type(board[counter_to_move+2][counter_to_movey+2]) == type(EmptySpace()):
                            print "Force-jump opertunity detected, excecutinga"
                            fjump = 1
                            time.sleep(3)
                            if type(board[counter_to_move][counter_to_movey]) == type(king):
                                board[counter_to_move+2][counter_to_movey+2] = king
                            elif type(board[counter_to_move][counter_to_movey]) == type(counter):
                                board[counter_to_move+2][counter_to_movey+2] = counter
                            board[counter_to_move][counter_to_movey] = EmptySpace()
                            board[counter_to_move+1][counter_to_movey+1] = EmptySpace()
                            counter_to_move = counter_to_move+2
                            counter_to_movey = counter_to_movey+2
                            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                                for row in board]))
                            counterlist.pop(0)
                            stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                            checkwin(friendlycounterlist, enemycounterlist)
                            break
            #Force jump logic to take a counter if it is possible bassed on the counter you selected
            if counter_to_move is not 7:
                if type(board[counter_to_move+1][counter_to_movey-1]) == type(ecounter) or type(board[counter_to_move+1][counter_to_movey-1]) == type(eking):
                    if type(board[counter_to_move+2][counter_to_movey-2]) == type(EmptySpace()):
                        print "Force-jump opertunity detected, excecuting"
                        fjump = 1
                        if type(board[counter_to_move][counter_to_movey]) == type(king):
                                    board[counter_to_move+2][counter_to_movey-2] = king
                        elif type(board[counter_to_move][counter_to_movey]) == type(counter):
                                    board[counter_to_move+2][counter_to_movey-2] = counter
                        time.sleep(3)
                        board[counter_to_move][counter_to_movey] = EmptySpace()
                        board[counter_to_move+1][counter_to_movey-1] = EmptySpace()
                        counter_to_move = counter_to_move+2
                        counter_to_movey = counter_to_movey-2
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                            for row in board]))
                        counterlist.pop(0)
                        stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                        checkwin(friendlycounterlist, enemycounterlist)
                        break
        break
        #This would be for the second turn function
        
        if secondturn == "1":
            print "second turn"
            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                    for row in board]))
            counter_to_move = counter_to_moveto
            counter_to_movey = counter_to_movetoy
            break
            
    valid_move = 0
    if fjump == 0:
        while valid_move == 0:
            #try:
            #While loops to take input and validate inputs of the space you want to move to
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
                    happy = raw_input("Are you happy with your selection? Y/N?: ")
                    if happy in ["N", "n"]:
                        continue
                    elif happy in ["y", "Y"]:
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
                    happy = raw_input("Are you happy with your selection? Y/N?: ")
                    if happy in ["N", "n"]:
                        continue
                    elif happy in ["y", "Y"]:
                        counter_to_movetoy = int(counter_to_move_toy_input)
                        break
            #Calculate displacement to be used for the counter taking logic
            a = (counter_to_move,counter_to_movey) 
            b = (counter_to_moveto,counter_to_movetoy)
            displacement = (a[0] - b[0], a[1] - b[1])
            #These ensure that you dont try to move to a space a counter is allready in        
            if type(board[counter_to_moveto][counter_to_movetoy]) == type(counter) or type(board[counter_to_moveto][counter_to_movetoy]) == type(eking) or type(board[counter_to_moveto][counter_to_movetoy]) == type(king) or type(board[counter_to_moveto][counter_to_movetoy]) == type(ecounter):
                print"There is already a counter in this position"
                continue
            #These two ensure each teams counters only do valid moves
            if player == "1":
                if type(board[counter_to_move][counter_to_movey]) == type(counter):
                    if counter_to_moveto is not counter_to_move-1: 
                        print "Not a valid move, blue counters can only move up the board" 
                        continue
            elif player == "2":
                if type(board[counter_to_move][counter_to_movey]) == type(counter):
                    if counter_to_moveto is not counter_to_move+1: 
                        print "Not a valid move, red counters can only move down the board" 
                        continue
            #Logic to ensure counters dont move to a counter dosent take an invalid move
            if counter_to_movetoy is not counter_to_movey +1:
                if counter_to_movetoy is not counter_to_movey -1:
                    if counter_to_movetoy is not counter_to_movey +2:
                        if counter_to_movetoy is not counter_to_movey -2:
                            if counter_to_movetoy is not counter_to_movey +3:
                                if counter_to_movetoy is not counter_to_movey -3:
                                    print "Not a valid move, counters can only move diagonally 1 or 3"
                                    continue
            #These are the logic's to take counters if it is a counter moving
            if type(board[counter_to_move][counter_to_movey]) == type(counter):
                if displacement == (2,-2):
                        if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                            board[counter_to_moveto+1][counter_to_movetoy-1] = EmptySpace()
                            board[counter_to_move][counter_to_movey] = EmptySpace()
                            board[counter_to_moveto][counter_to_movetoy] = counter
                            valid_move = 1;
                            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                                for row in board]))
                            counterlist.pop(0)
                            stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                            checkwin(friendlycounterlist, enemycounterlist)
                        if type(board[counter_to_moveto-1][counter_to_movetoy+1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):    
                            if type(board[counter_to_moveto-2][counter_to_movetoy+2]) == type(EmptySpace()):
                                secondturn = "1"
                                userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)
                                break
                        elif type(board[counter_to_move][counter_to_movey]) == type(counter): 
                            if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king):
                                print "Not a valid move-"
                                continue
                        elif type(board[counter_to_move][counter_to_movey]) == type(king):
                            if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(king):
                                print "Not a valid move--"
                                continue
                #Taking counters bassed on displacements                   
                if displacement == (2,2):
                    if type(board[counter_to_moveto+1][counter_to_movetoy+1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy+1]) == type(eking):
                            board[counter_to_move][counter_to_movey] = EmptySpace()
                            board[counter_to_moveto+1][counter_to_movetoy+1] = EmptySpace()
                            if type(board[counter_to_move][counter_to_movey]) == type(king):
                                board[counter_to_moveto][counter_to_movetoy] = king
                            else:
                                board[counter_to_moveto][counter_to_movetoy] = counter
                            valid_move = 1;   
                            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                              for row in board]))
                            counterlist.pop(0)
                            stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                            checkwin(friendlycounterlist, enemycounterlist)
                    if type(board[counter_to_moveto-1][counter_to_movetoy-1]) == type(ecounter):   
                        if type(board[counter_to_moveto-2][counter_to_movetoy-2]) == type(EmptySpace()):
                            secondturn == "1"
                            print "kss"
                            userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)       
                #Taking counters bassed on displacements 
                if displacement == (-2,-2):
                        if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                                board[counter_to_moveto-1][counter_to_movetoy-1] = EmptySpace()
                                board[counter_to_move][counter_to_movey] = EmptySpace()
                        if type(board[counter_to_move][counter_to_movey]) == type(king):
                            board[counter_to_moveto][counter_to_movetoy] = king
                        else:
                            board[counter_to_moveto][counter_to_movetoy] = counter
                        valid_move = 1;
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                            for row in board]))
                        print "counters taken =: " 
                        counterlist.pop(0)
                        stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                        checkwin(friendlycounterlist, enemycounterlist)
                        if type(board[counter_to_moveto-1][counter_to_movetoy+1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):    
                            if type(board[counter_to_moveto-2][counter_to_movetoy+2]) == type(EmptySpace()):
                                secondturn = "1"
                                userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)
                                break
                        elif type(board[counter_to_move][counter_to_movey]) == type(counter): 
                            if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king):
                                print "Not a valid move-"
                                continue
                        elif type(board[counter_to_move][counter_to_movey]) == type(king):
                            if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(king):
                                print "Not a valid move--"
                                continue
                #Taking counters bassed on displacements 
                if displacement == (-2,2):
                    if type(board[counter_to_moveto-1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto-1][counter_to_movetoy+1]) == type(eking) or type(board[counter_to_moveto-1][counter_to_movetoy+1]) == type(ecounter) or type(board[counter_to_moveto-1][counter_to_movetoy-1]) == type(eking):
                        board[counter_to_moveto-1][counter_to_movetoy+1] = EmptySpace()
                        board[counter_to_move][counter_to_movey] = EmptySpace()
                        if type(board[counter_to_move][counter_to_movey]) == type(king):
                            board[counter_to_moveto][counter_to_movetoy] = king
                        else:
                            board[counter_to_moveto][counter_to_movetoy] = counter
                        valid_move = 1;    
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                        counterlist.pop(0)
                        stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                        checkwin(friendlycounterlist, enemycounterlist)
                    if type(board[counter_to_moveto-1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):    
                        if type(board[counter_to_moveto-2][counter_to_movetoy-2]) == type(EmptySpace()):
                            secondturn = "1"
                            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                                for row in board]))
                            userturnlogic(counter_to_moveto, counter_to_movetoy, secondturn, player, turn, counterstaken, board, player2counterstaken)
                    elif type(board[counter_to_moveto-1][counter_to_movetoy+1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):    
                            if type(board[counter_to_moveto-2][counter_to_movetoy+2]) == type(EmptySpace()):
                                secondturn = "1"
                                userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)
                                break
                    elif type(board[counter_to_move][counter_to_movey]) == type(counter): 
                        if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king):
                            print "Not a valid move, you cant jump your own counter"
                            continue
                    elif type(board[counter_to_move][counter_to_movey]) == type(king):
                        if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(king):
                            print "Not a valid move, you cant jump your own counter"
                            continue
            #Taking counters if its a king moving
            if type(board[counter_to_move][counter_to_movey]) == type(king):    
                if displacement == (2,-2):
                        if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                            board[counter_to_moveto+1][counter_to_movetoy-1] = EmptySpace()
                            board[counter_to_move][counter_to_movey] = EmptySpace()
                            board[counter_to_moveto][counter_to_movetoy] = king
                            valid_move = 1;
                            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                              for row in board]))
                            print "king"
                            counterlist.pop(0)
                            stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                            checkwin(friendlycounterlist, enemycounterlist)
                        if type(board[counter_to_moveto-1][counter_to_movetoy+1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):    
                            if type(board[counter_to_moveto-2][counter_to_movetoy+2]) == type(EmptySpace()):
                                secondturn = "1"
                                userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)
                                break
                        elif type(board[counter_to_move][counter_to_movey]) == type(counter): 
                            if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king):
                                print "Not a valid move, you cant jump your own counter"
                                continue
                        elif type(board[counter_to_move][counter_to_movey]) == type(king):
                            if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(king):
                                print "Not a valid move, you cant jump your own counter"
                                continue
                #Taking counters bassed on displacements
                if displacement == (2,2):
                    if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                        board[counter_to_moveto+1][counter_to_movetoy+1] = EmptySpace()
                        board[counter_to_move][counter_to_movey] = EmptySpace()
                        if type(board[counter_to_move][counter_to_movey]) == type(king):
                            board[counter_to_moveto][counter_to_movetoy] = king
                        else:
                            board[counter_to_moveto][counter_to_movetoy] = counter
                        valid_move = 1;    
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                        counterlist.pop(0)
                        stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                        checkwin(friendlycounterlist, enemycounterlist)
                    if type(board[counter_to_moveto-1][counter_to_movetoy+1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):    
                            if type(board[counter_to_moveto-2][counter_to_movetoy+2]) == type(EmptySpace()):
                                secondturn = "1"
                                userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)
                                break
                    if type(board[counter_to_move][counter_to_movey]) == type(counter): 
                        if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king):
                            print "Not a valid move, you cant jump your own counter"
                            continue
                    if type(board[counter_to_move][counter_to_movey]) == type(king):
                        if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(king):
                            print "Not a valid move, you cant jump your own counter"
                            continue
                #Taking counters bassed on displacements
                if displacement == (-2,-2):
                        if type(board[counter_to_moveto-1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto-1][counter_to_movetoy-1]) == type(eking):
                            board[counter_to_moveto-1][counter_to_movetoy-1] = EmptySpace()
                            board[counter_to_move][counter_to_movey] = EmptySpace()
                            board[counter_to_moveto][counter_to_movetoy] = king
                        valid_move = 1;
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                        counterlist.pop(0)
                        stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                        checkwin(friendlycounterlist, enemycounterlist)
                        userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)
                        if type(board[counter_to_moveto-1][counter_to_movetoy+1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):    
                            if type(board[counter_to_moveto-2][counter_to_movetoy+2]) == type(EmptySpace()):
                                secondturn = "1"
                                userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)
                                break
                        elif type(board[counter_to_move][counter_to_movey]) == type(counter): 
                            if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king):
                                print "Not a valid move, you cant jump your own counter7"
                                continue
                        elif type(board[counter_to_move][counter_to_movey]) == type(king):
                            if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(king):
                                print "Not a valid move, you cant jump your own counter8"
                                continue
                #Taking counters bassed on displacements
                if displacement == (-2,2):
                    if type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):
                        board[counter_to_moveto-1][counter_to_movetoy+1] = EmptySpace()
                        board[counter_to_move][counter_to_movey] = EmptySpace()
                        if type(board[counter_to_move][counter_to_movey]) == type(king):
                            board[counter_to_moveto][counter_to_movetoy] = king
                        else:
                            board[counter_to_moveto][counter_to_movetoy] = counter
                        valid_move = 1;    
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                        counterlist.pop(0)
                        stalematelist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                        checkstalemate(stalematelist)
                        checkwin(friendlycounterlist, enemycounterlist)
                        userturnlogic(counter_to_moveto, counter_to_movetoy, secondturn, player, turn, counterstaken, board, player2counterstaken)
                    if type(board[counter_to_moveto-1][counter_to_movetoy+1]) == type(ecounter) or type(board[counter_to_moveto+1][counter_to_movetoy-1]) == type(eking):    
                        if type(board[counter_to_moveto-2][counter_to_movetoy+2]) == type(EmptySpace()):
                            secondturn = "1"
                            userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)
                            break
                    elif type(board[counter_to_move][counter_to_movey]) == type(counter): 
                        if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king):
                            print "Not a valid move, you cant jump your own counter9"
                            continue
                    elif type(board[counter_to_move][counter_to_movey]) == type(king):
                        if board[counter_to_moveto+1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto+1][counter_to_movetoy+1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy-1] == type(king) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(counter) or board[counter_to_moveto-1][counter_to_movetoy+1] == type(king):
                            print "Not a valid move, you cant jump your own counter10"
                            continue
            if player == "1":
                if board[counter_to_moveto+1][counter_to_movetoy-1] == counter:
                    if counter_to_moveto is counter_to_move - 2 or counter_to_movetoy is counter_to_movey - 2  :
                        print"Not a valid move---"
                        continue
            if counter_to_moveto == counter_to_move - 1 and counter_to_movetoy == counter_to_movey:
                print "Not a valid move, counters can only move diagonaly"
                continue
            #Not allowing moves to the top and side of the board
            if board[counter_to_moveto][counter_to_movetoy] == "      " or board[counter_to_moveto][counter_to_movetoy] == "   1   " or board[counter_to_moveto][counter_to_movetoy] == "     2    " or board[counter_to_moveto][counter_to_movetoy] == "    3    " or board[counter_to_moveto][counter_to_movetoy] == "    4    " or board[counter_to_moveto][counter_to_movetoy] == "   5   " or board[counter_to_moveto][counter_to_movetoy] == "      6   " or board[counter_to_moveto][counter_to_movetoy] == "    7    " or board[counter_to_moveto][counter_to_movetoy] == "    8    ":
                print"Not a valid position" 
                continue
            #Movement that is not taking a counter for each team
            if player == "1":
                if counter_to_moveto == 1:
                    board[counter_to_moveto][counter_to_movetoy] = king
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                              for row in board]))
                    break
            if player == "2":
                if counter_to_moveto == 8:
                    board[counter_to_moveto][counter_to_movetoy] = king
                    board[counter_to_move][counter_to_movey] = EmptySpace()
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                          for row in board]))
                    break
            elif type(board[counter_to_move][counter_to_movey]) == type(king):
                board[counter_to_move][counter_to_movey] = EmptySpace()
                board[counter_to_moveto][counter_to_movetoy] = king
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                stalematelist.pop(0)
                checkstalemate(stalematelist)
                valid_move = 1
            if type(board[counter_to_move][counter_to_movey]) == type(counter):
                board[counter_to_move][counter_to_movey] = EmptySpace()
                board[counter_to_moveto][counter_to_movetoy] = counter
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                      for row in board]))
                stalematelist.pop(0)
                checkstalemate(stalematelist)
                valid_move = 1
        reversedisplacement = (displacement[0], displacement[1])
    #Call the undo function
    undofuncion(stalematelist, replaylist, turn, board,counter_to_move,counter_to_movey, counter_to_moveto,counter_to_movetoy, movelist, redolist)
   


def undofuncion(stalematelist, replaylist, turn, board,counter_to_move,counter_to_movey, counter_to_moveto,counter_to_movetoy, movelist, redolist):
    #Setting up the function for each team
    if turn == "Player 1":
        mlist = movelist
        rlist = redolist
        counter = FriendlyCounter()
        counterlist = friendlycounterlist
        king = FriendlyKing()
    else:
        mlist = player2movelist
        rlist = player2redolist
        counter = EnemyCounter()
        king = EnemyKing()
        counterlist = enemycounterlist
    #Save the move last made move to a list
    startposx = counter_to_move
    startposy = counter_to_movey
    endposx = counter_to_moveto 
    endposy = counter_to_movetoy 
    startpos = (startposx, startposy)
    endpos = (endposx, endposy)
    move = (startpos, endpos)
    mlist.insert(0,move)
    replaylist.append(move)
    #This while loop undo's the move by taking it from a list, and revesrsing it then adding the move to a replay list
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
                        stalematelist.insert(0,1)
                        counterlist.insert(0,1)
                        rlist.append(i)
                        mlist.remove(i)
                        continue
            else:
                break
            #If theres a move in the redo list, allow the user the option to redo the move
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
                        if x == 8 or x == 1:
                            board[x][y] = king
                        else:
                            board[x][y] = counter

                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
                                for row in board]))
                        counterlist.pop(0)
                        stalematelist.pop(0)
                        rlist.remove(i)
                        continue
            else:
                break
        else:
            break
def AIturnlogic(board):
    print "AI Incomplete"
def replay(replayboard, replaylist):
    #If the user wants to replay the game, print the board and begin the replay
    replay = raw_input("Press P to begin the replay: ")
    if replay in ['p', 'P']:
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in replayboard]))
        for i in replaylist:
            #play through the game automatically, move by move
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
    #Print the you win ascii art then call replay, the return to main menu
    text = [["|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | ||  |"], 
            ["|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| ||  |"], 
            ["|       ||  | |  ||  |_|  |  |       ||   | |       ||  |"], 
            ["|_     _||  |_|  ||       |  |       ||   | |  _    ||__| "],
              ["|   |  |       ||       |  |   _   ||   | | | |   | __  "],
              ["|___|  |_______||_______|  |__| |__||___| |_|  |__||__|"]]

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in text]))
    replay(replayboard, replaylist)
    main()
def youlose():
    #Print the you lose ascii art then call replay, the return to main menu
    youloset = [["|  | |  ||       ||  | |  |  |   |    |       ||       ||       |  |   |  |    |"], 
                ["|  |_|  ||   _   ||  | |  |  |   |    |   _   ||  _____||    ___|  |___| |    _|"], 
                ["|       ||  | |  ||  |_|  |  |   |    |  | |  || |_____ |   |___    ___  |   |"],   
                ["|_     _||  |_|  ||       |  |   |___ |  |_|  ||_____  ||    ___|  |   | |   |"],   
                  ["|   |  |       ||       |  |       ||       | _____| ||   |___   |___| |   |_"],  
                  ["|___|  |_______||_______|  |_______||_______||_______||_______|         |____|"]]
      
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in youloset]))
    replay(replayboard, replaylist)
    main()
def Player1(player):
        #set the player variable to 1 to set up the turn function
        player = "1"
        counter_to_moveto = 1
        counter_to_movetoy = 3
        userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)

def Player2(player):
    #set the player variable to 2 to set up the turn function
        player = "2"
        counter_to_moveto = 1
        counter_to_movetoy = 3
        userturnlogic(stalematelist, counter_to_moveto, counter_to_movetoy, secondturn, player, turn, board)

def checkwin(friendlycounterlist, enemycounterlist):
    #If the counterlist is emoty, enemy wins
    if not friendlycounterlist:
        youwin()
        replay(replayboard, replaylist)
    else:
        #if the enemycounterlist is empty, friendly wins
        if not enemycounterlist:
            youlose()
            replay(replayboard, replaylist)
def draw(board):
    #print the draw ascii art the czll the replay function
    drawt = [["_______  .______          ___   ____    __    ____ "],
            ["|       \ |   _  \        /   \  \   \  /  \  /   / "],
            ["|  .--.  ||  |_)  |      /  ^  \  \   \/    \/   /  "],
            ["|  |  |  ||      /      /  /_\  \  \            /   "],
            ["|  '--'  ||  |\  \----./  _____  \  \    /\    /    "],
            ["|_______/ | _| `._____/__/     \__\  \__/  \__/     "]]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in drawt]))
    replay(replayboard, replaylist)
    main()                                                
def checkstalemate(stalematelist):
    #checks if therer has not been a coiunter taken in 25 moves then declare a stalemate
    if not stalematelist:
        draw(board)
def main():
    print("Alistair Mckay")
    print("40207511")
    print("Algorithms & Data Structures Coursework")
    print("Enter co-ordinates of counter in the form (vertical,horizontal)")
    undo_no = ""
    while True:
        #take an iput and validate it
        begin = raw_input("Press 1 to play with against the computer, 2 to play against another person, T for tutorial, N to quit: ")
        if begin  ==  "N":
            sys.exit()
        elif begin  not in ['1', '2', 't', 'T']:
            print"Please enter 1, 2, or N only"
            continue
        elif begin in ['t', 'T']:
            tutorial()
            continue
        elif begin == '1':
            print"Human"
            
            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
              for row in board]))
            #player 1 loop
            while True:
                Player1(player)
                Player2(player)
            youwin()
        #AI does not currently work
        elif begin == '2':
            print "AI"
            
            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
              for row in board]))
                
        while True:
            #player 2 loop
            Player1(player)
            AIturnlogic(board, aicounterstaken)
        youwin()
#the function that runs it all
main()