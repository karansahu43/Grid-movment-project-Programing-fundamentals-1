# Program: Grid movement test 
# Description: 
# 	moving the game peice on a grid
# Author: Karan Sahu
# Date: 9/15/2017
# Revised: 
# 	<revision date> 

# list libraries used

# Declare global constants

#Main Program

##Declare variables
gamePieceRow = 5
gamePieceColumn = 5

##Set up the movement test
moveDirection = 0
moveDistance = 0

##Move the game piece and display its position
gamePieceRow = gamePieceRow + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )

##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow + moveDistance
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow + moveDistance
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Reset the direction and increase the distance
moveDirection = 0
moveDistance = 1

##Move the game piece and display its position
gamePieceRow = gamePieceRow + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow + moveDistance
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow + moveDistance
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Reset the direction and increase the distance
moveDirection = 0
moveDistance = 2

##Move the game piece and display its position
gamePieceRow = gamePieceRow + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow + moveDistance
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow + moveDistance
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Reset the direction and increase the distance
moveDirection = 0
moveDistance = 3

##Move the game piece and display its position
gamePieceRow = gamePieceRow + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow + moveDistance
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
gamePieceColumn = gamePieceColumn + moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow - moveDistance
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )


##Increase the direction, move the game piece and display its position
moveDirection = moveDirection + 1
gamePieceRow = gamePieceRow + moveDistance
gamePieceColumn = gamePieceColumn - moveDistance
print ("The game piece is at row " + str(gamePieceRow) + ", and colum " + str(gamePieceColumn) )



#End Program



    // Declare variables
    Set gamePieceRow to 5
    Set gamePieceColumn to 5

    // Set up the movement test
    Set moveDirection = 0
    Set moveDistance = 0

    // Move the game piece and display its position
    Set gamePieceRow = gamePieceRow + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn


    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow + moveDistance
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Set gamePieceColumn = gamePieceColumn - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceColumn = gamePieceColumn - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow + moveDistance
    Set gamePieceColumn = gamePieceColumn – moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Reset the direction and increase the distance
    Set moveDirection = 0
    Set moveDistance = 1

    // Move the game piece and display its position
    Set gamePieceRow = gamePieceRow + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow + moveDistance
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Set gamePieceColumn = gamePieceColumn - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceColumn = gamePieceColumn - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow + moveDistance
    Set gamePieceColumn = gamePieceColumn – moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Reset the direction and increase the distance
    Set moveDirection = 0
    Set moveDistance = 2

    // Move the game piece and display its position
    Set gamePieceRow = gamePieceRow + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow + moveDistance
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Set gamePieceColumn = gamePieceColumn - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceColumn = gamePieceColumn - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow + moveDistance
    Set gamePieceColumn = gamePieceColumn – moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Reset the direction and increase the distance
    Set moveDirection = 0
    Set moveDistance = 3

    // Move the game piece and display its position
    Set gamePieceRow = gamePieceRow + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow + moveDistance
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Set gamePieceColumn = gamePieceColumn + moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow - moveDistance
    Set gamePieceColumn = gamePieceColumn - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceColumn = gamePieceColumn - moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

    // Increase the direction, move the game piece and display its position
    Set moveDirection = moveDirection + 1
    Set gamePieceRow = gamePieceRow + moveDistance
    Set gamePieceColumn = gamePieceColumn – moveDistance
    Display “The game piece is at row “, gamePieceRow, “ and column “, gamePieceColumn

