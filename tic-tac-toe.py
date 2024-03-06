from random import randint

table = [['|', '-', '|'],
         ['-', '+', '-'],
         ['|', '-', '|']
         ]

# checks all possible win conditions for tic tac toe
def winCheck():
    for i in range(len(table)):
        if table[i][0] == table[i][1] and table[i][0] == table[i][2]:
            return 'n'
        elif table[0][i] == table[1][i] and table[0][i] == table[2][i]:
            return 'n'

    if table[0][0] == table[1][1] and table[0][0] == table[2][2]:
        return 'n' 
    if table[0][2] == table[1][1] and table[0][2] == table[2][0]:
        return 'n'
    
    if ('|' or '+' or '-') not in table[0] and ('|' or '+' or '-') not in table[1] and ('|' or '+' or '-') not in table[2]:
        return 'n'

    return 'y'

# chooses random position for the computers move (note computer is always 'X')
def computerMove():

    computer_row = randint(0,2)
    computer_column = randint(0,2)

    if table[computer_row][computer_column] == '|' or table[computer_row][computer_column] == '-' or table[computer_row][computer_column] == '+':
        table[computer_row][computer_column] = 'X'
    else: 
         computerMove()

# takes inputs for the players move (note the player is always 'O')
def playerMove():
    player_row = int(input('Which row do you want (0-2)?: '))
    player_column = int(input('What column do you want (0-2?): '))

    if table[player_row][player_column] == '|' or table[player_row][player_column] == '-' or table[player_row][player_column] == '+':
        table[player_row][player_column] = 'O'
    else:
         playerMove()
        
def printTable():
        for i in range(len(table)):
            print(table[i])


play = 'y'

# for simplicity, the computer always goes first
# this could easily be changed but break time was up 

while play != 'n':

    computerMove()
    printTable()

    print()

    play = winCheck()
    
    if play != 'n':
        playerMove()
        printTable()

        print()

    play = winCheck()


print('Good game!')
printTable()
