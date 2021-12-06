# First step printing UI

def drawFields():
    for row in range(5):
        if row % 2 == 0:
            for column in range(5):
                if column % 2 == 0:
                    if column != 4:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print("-----")


Player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

while(True):
    print("Player turn: ", Player)
    MoveType = input("Enter your move type(X/O): ")
    MoveRow = int(input("Please enter the row: "))
    MoveColumn = int(input("Please enter the column: "))
    if Player == 1:
        currentField[MoveColumn][MoveRow] = MoveType
        Player = 2
    else:
        currentField[MoveColumn][MoveRow] = MoveType
        Player = 1
    print(currentField)
