import sys

player = 'O'
bot = 'X'


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def printBoard(board, letter):
    print(letter + "'s turn")
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

        
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board, letter)
        if checkDraw():
            print("Draw!")           
            sys.exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                sys.exit()
            else:
                print("Player wins!")
                sys.exit()
        return
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return


def checkForWin():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
        return True
    else:
        return False


def checkMark(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] == mark:
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def playerMove():
    position = int(input("Enter the position for 'O':  "))
    print('\n')
    insertLetter(player, position)
    return


def compMove():
    bestScore = -1000
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter(bot, bestMove)
    return


def minimax(board, isMaximizing):
    if checkMark(bot):
        return 1
    elif checkMark(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore 

    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


print("\nPositions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print('\n') 
print('You are O and the computer is X') 
printBoard(board, 'Good Luck')

def game():
    first = input('Do you want to go first?(y/n): ')
    if first == 'y':
        while not checkForWin():
            playerMove()
            compMove()
    elif first == 'n':
        while not checkForWin():
            compMove()
            playerMove()
    else:
        print('Please enter y/n')
        game() 
        
game()





    
    
