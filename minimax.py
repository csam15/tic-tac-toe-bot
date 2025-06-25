import sys

player = 'X'
ai = 'O'

#Empty game board
theboard = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 

#Prints the tic tac toe board
def printboard(board):
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('-+-+-')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2]) 
    print('-+-+-')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2] + '\n')
   
        
def endGame(b):
    print('\n\nThe game has ended!')
    x = input("Would you like to play again?(y/n) ")
    if x == 'y':
        b = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
        theGame(b)
    if x == 'n':
        print('Thank you for playing!')
        sys.exit()
    else:
        print('Please answer using y/n')
        endGame(b)
   
#Determines if there is any moves left 
def movesLeft(b):
    x = 0
    for row in range(3):
        for col in range(3):
            if b[row][col] != ' ':
                x += 1
    if x == 9:
        return False
    elif x < 9:
        return True
    
def evalBoard(b):
    A = evaluate(b)
    B = movesLeft(b) 
    if A != None or B == False:
        printboard(b)
        endGame(b)
    
#Evaluation function
def evaluate(b):
    
    #Check for victory in rows
    for row in range(3):
        if (b[row][0] == b[row][1] == b[row][2]):       
            if b[row][0] == 'X':
                return 1
            elif b[row][0] == 'O': 
                return -1
          
    #Check for victory in columns
    for col in range(3) :
        if (b[0][col] == b[1][col] == b[2][col]):
            if b[0][col] == 'X':
                return 1
            elif b[0][col] == 'O':
                return -1
    
    #Check for victory in diagonals
    if (b[0][0] == b[1][1] == b[2][2]) :
        if b[0][0] == 'X':
            return 1
        elif b[0][0] == 'O':
            return -1
 
    if (b[0][2] == b[1][1] == b[2][0]):
        if b[0][2] == 'X':
            return 1
        elif b[0][2] == 'O':
            return -1
        

def minimax(b, depth, isMax):
	score = evaluate(b)

	if score == 1:
		return score

	if score == -1:
		return score

	if movesLeft(b) == False:
		return 0
    
	if isMax:	
		best = -1000
		for r in range(3):		
			for c in range(3):
				if b[r][c]==' ':
					b[r][c] = player
					best = max(best, minimax(b, depth + 1, not isMax))
					b[r][c] = ' '
		return best-depth

	else :
		best = 1000
		for r in range(3):		
			for c in range(3):
				if b[r][c] == ' ':
					b[r][c] = ai
					best = min(best, minimax(b, depth + 1, not isMax))
					b[r][c] = ' '
		return best+depth

def findBestMove(b):
    bestVal = -100
    bestMove = (-1,-1)
    
    for r in range(3):
        for c in range(3):
            if b[r][c] == ' ':
                b[r][c] = 'X'
                moveVal = minimax(b, 0, True)
                b[r][c] = ' '
                if moveVal > bestVal:
                    bestMove = (r,c)
                    bestVal = moveVal
    return bestMove

#User play
def player(b):
    movesLeft(b)
    evaluate(b)
    playChoice = input('Where do you wanna place your X?: ')
    if playChoice == '1':
        b[0][0] = 'X' 
    elif playChoice == '2':
        b[0][1] = 'X'
    elif playChoice == '3':
        b[0][2] = 'X'
    elif playChoice == '4':
        b[1][0] = 'X'
    elif playChoice == '5':
        b[1][1] = 'X'
    elif playChoice == '6':
        b[1][2] = 'X'
    elif playChoice == '7':
        b[2][0] = 'X'
    elif playChoice == '8':
        b[2][1] = 'X'
    elif playChoice == '9':
        b[2][2] = 'X'
    else:
        print('Please enter a valid value (1-9)')

#THE GAME
def theGame(b):
    print('Welcome to Tic Tac Toe!')
    first = input('You are X, and the AI is O\nWould you like to go first?(y/n) ')
    if first == 'y':
       while True:
           evalBoard(b)
           player(b)
           evalBoard(b)
           printboard(b)
           M = findBestMove(b)
           b[M[0]][M[1]] = 'O'
           printboard(b) 
    if first == 'n':
        while True:
            evalBoard(b)            
            M = findBestMove(b)
            b[M[0]][M[1]] = 'O'
            printboard(b)
            evalBoard(b)
            player(b)
            printboard(b) 
    else:
        print('Please enter y/n')
        theGame(b)        
               
theGame(theboard)
    
    
    
    
    
    
    
    



