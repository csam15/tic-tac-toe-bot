#tic tac toe bitch

theboard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

def printboard(board):
    print(board['7'] + ' |' + board['8'] + '|' + board['9'])
    print('--+-+--')
    print(board['4'] + ' |' + board['5'] + '|' + board['6']) 
    print('--+-+--')
    print(board['1'] + ' |' + board['2'] + '|' + board['3'])
    
print('Welcome to Tic-Tac-Toe!\nTo choose your spot on the board, use the numbers on your keyboard as follows:\n7 8 9\n4 5 6\n1 2 3')

player1 = 'X'
player2 = 'O'
count = 0

for i in range(10):
    printboard(theboard)
    if i % 2 == 0:
        choice1 = input('It is your turn ' + player1 + ', please select a spot to place your X: ')
        theboard[choice1] = player1
    else:
        choice2 = input('It is your turn ' + player2 + ', please select a spot to place your O: ')
        theboard[choice2] = player2
    count += 1
    
    if count >= 5:
        if theboard['7'] == theboard['8'] == theboard['9'] != ' ': # across the top
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" You won!!!!")                
                break
        elif theboard['4'] == theboard['5'] == theboard['6'] != ' ': # across the middle
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" You won!!!!")
                break
        elif theboard['1'] == theboard['2'] == theboard['3'] != ' ': # across the bottom
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" You won!!!!")
                break
        elif theboard['1'] == theboard['4'] == theboard['7'] != ' ': # down the left side
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" You won!!!!")
                break
        elif theboard['2'] == theboard['5'] == theboard['8'] != ' ': # down the middle
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" You won!!!!")
                break
        elif theboard['3'] == theboard['6'] == theboard['9'] != ' ': # down the right side
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" You won!!!!")
                break 
        elif theboard['7'] == theboard['5'] == theboard['3'] != ' ': # diagonal
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" You won!!!!")
                break
        elif theboard['1'] == theboard['5'] == theboard['9'] != ' ': # diagonal
                printboard(theboard)
                print("\nGame Over.\n")                
                print(" You won!!!!")
                break 

    
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
        
    