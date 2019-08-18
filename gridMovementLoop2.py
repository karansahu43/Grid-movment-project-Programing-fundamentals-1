# Program: Grid movement test 3
# Description: 
#  	moving the game peice on a grid using functions
# Author: Karan Sahu
# Date: 10/23/2017
# Revised: 
#  	10/24/2017

# list libraries used

# Declare global constants

# Main Program

def main():

    # Declare variables
    gamePieceRow = 5
    gamePieceColumn = 5
    moveDirection = 0
    moveDistance = 0


    
    # Set range for distance moved
    for moveDistance in range (4):
        print()
        # set range for directions moved
        for moveDirection in range (8):
            
            gamePieceRow, gamePieceColumn = movePiece(gamePieceRow, gamePieceColumn, moveDistance, moveDirection)

            
            # Print game piece position
            print ("The game piece is at row ", gamePieceRow, " and column ", gamePieceColumn)
        # End for

    #End for

#End program


# Function movePiece 
# Description:
#	calculate and returns gamePieceRow and gamePieceColumn
# Calls:
#	none
# Parameters:
#	 gamePieceRow
#        gamePieceColumn
#        moveDistance
#        moveDirection
# Returns:
#	gamePieceRow
#       gamePieceColumn


 
def movePiece(gamePieceRow, gamePieceColumn, moveDistance, moveDirection):


    # Declare local variables
              

        # Set directions

    if (moveDirection == 0):

        # Move the game piece N

        gamePieceRow = gamePieceRow + moveDistance
        gamePieceColumn = gamePieceColumn + 0

        # Return values  

        return(gamePieceRow, gamePieceColumn)


    

    elif (moveDirection == 1):

        # move the game piece NE

        gamePieceRow = gamePieceRow + moveDistance
        gamePieceColumn = gamePieceColumn + moveDistance

        # Return values  

        return(gamePieceRow, gamePieceColumn)



    elif (moveDirection == 2):

        # move the game piece E

        gamePieceColumn = gamePieceColumn + moveDistance
        gamePieceRow = gamePieceRow + 0

        # Return values  

        return(gamePieceRow, gamePieceColumn)



    elif (moveDirection == 3):

        # move the game piece SE

        gamePieceRow = gamePieceRow - moveDistance
        gamePieceColumn = gamePieceColumn + moveDistance

        # Return values  

        return(gamePieceRow, gamePieceColumn)




    elif (moveDirection == 4):

        # move the game piece S

        gamePieceRow = gamePieceRow - moveDistance
        gamePieceColumn = gamePieceColumn + 0

        # Return values  

        return(gamePieceRow, gamePieceColumn)



    elif (moveDirection == 5):

        # move the game piece SW

        gamePieceRow = gamePieceRow - moveDistance
        gamePieceColumn = gamePieceColumn - moveDistance

        # Return values  

        return(gamePieceRow, gamePieceColumn)



    elif (moveDirection == 6):

        # move the game piece W

        gamePieceColumn = gamePieceColumn - moveDistance
        gamePieceRow = gamePieceRow + 0

        # Return values  

        return(gamePieceRow, gamePieceColumn)



    elif (moveDirection == 7):

        # move the game piece NW

        gamePieceRow = gamePieceRow + moveDistance 
        gamePieceColumn = gamePieceColumn - moveDistance

        # Return values  

        return(gamePieceRow, gamePieceColumn)





    #End if 


# End function


main()





  
