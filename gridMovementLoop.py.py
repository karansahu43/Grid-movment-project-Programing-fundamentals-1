# Program: Grid movement test 2
# Description: 
#  	moving the game peice on a grid
# Author: Karan Sahu
# Date: 10/5/2017
# Revised: 
#  	<revision date> 

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
       
        # set range for all directions moved
        for moveDirection in range (8):
                    

            # Set directions

            if (moveDirection == 0):

                # Move the game piece and print its position N

                gamePieceRow = gamePieceRow + moveDistance

                print ("The game piece is at row ", gamePieceRow, " and column ", gamePieceColumn)

            

            elif (moveDirection == 1):

                # move the game piece and print its position NE

                gamePieceRow = gamePieceRow + moveDistance
                gamePieceColumn = gamePieceColumn + moveDistance

                print ("The game piece is at row ", gamePieceRow, " and column ", gamePieceColumn)


            elif (moveDirection == 2):

                # move the game piece and print its position E

                gamePieceColumn = gamePieceColumn + moveDistance

                print ("The game piece is at row ", gamePieceRow, " and column ", gamePieceColumn)


            elif (moveDirection == 3):

                # move the game piece and print its position SE

                gamePieceRow = gamePieceRow - moveDistance
                gamePieceColumn = gamePieceColumn + moveDistance

                print ("The game piece is at row ", gamePieceRow, " and column ", gamePieceColumn)


            elif (moveDirection == 4):

                # move the game piece and print its position S

                gamePieceRow = gamePieceRow - moveDistance

                print ("The game piece is at row ", gamePieceRow, " and column ", gamePieceColumn)


            elif (moveDirection == 5):

                # move the game piece and print its position SW

                gamePieceRow = gamePieceRow - moveDistance
                gamePieceColumn = gamePieceColumn - moveDistance

                print ("The game piece is at row ", gamePieceRow, " and column ", gamePieceColumn)


            elif (moveDirection == 6):

                # move the game piece and print its position W

                gamePieceColumn = gamePieceColumn - moveDistance

                print ("The game piece is at row ", gamePieceRow, " and column ", gamePieceColumn)


            elif (moveDirection == 7):

                # move the game piece and print its position NW

                gamePieceRow = gamePieceRow + moveDistance 
                gamePieceColumn = gamePieceColumn - moveDistance

                print ("The game piece is at row ", gamePieceRow, " and column ", gamePieceColumn)




            #End if 

                    
        #End for

    #End for



#End program

main()





  
