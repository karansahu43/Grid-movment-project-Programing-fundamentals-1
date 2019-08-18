
# Program: Grid movement test 
# Description: 
#  	moving the game peice on a grid using lists
# Author: Karan Sahu
# Date: 9/15/2017
# Revised: 
#  	<revision date> 

# list libraries used

# Declare global constants
N = [1, 0]
NE = [1, 1]
E = [0, 1]
SE = [-1, 1]
S = [-1, 0]
SW = [-1, -1]
W = [0, -1]
NW = [1, -1]
MOVEMENT = [N, NE, E, SE, S, SW, W, NW]
gamePiece = [5, 5]
ROW = 0
COL = 1



def main():

    # Declare variables
    ROWS = 15
    COLS = 15
    item = 0

    gameBoard = ['.'] * ROWS
    
    # Set up movement test
    moveDirection = 0
    moveDistance = 0

    for item in range(COLS):
        gameBoard[item] = ['.'] * COLS
        print(gameBoard[item])
    #End For

    for moveDistance in range (4):
        for moveDirection in range (8):
            
            gamePiece [ROW] = gamePiece [ROW] + MOVEMENT [moveDirection] [ROW] * moveDistance
            gamePiece [COL]   = gamePiece [COL]   + MOVEMENT [moveDirection] [COL] * moveDistance

            gameBoard[gamePiece [ROW]][gamePiece [COL]] = 'X'
            
            print("The game piece is at row ", gamePiece[ROW] , " and column ", gamePiece[COL])
        #End for
    #End for
    for row in gameBoard:
        for column in row:
            print(column, end = ' ')
        #End for

        print ()
    #End for

# End main function

main()
