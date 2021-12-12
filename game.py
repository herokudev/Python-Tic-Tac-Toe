# First step printing UI

def drawFields(field):
    for row in range(5):
        if row % 2 == 0:
            fieldRow = int(row / 2)
            for column in range(5):  # 0,1,2,3,4 --> 0,.,1,.,2
                if column % 2 == 0:  # 0,2,4
                    fieldColumn = int(column / 2)  # 0,1,2
                    if column != 4:
                        print(field[fieldColumn][fieldRow], end="")
                    else:
                        print(field[fieldColumn][fieldRow])
                else:
                    print("|", end="")
        else:
            print("-----")


Player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawFields(currentField)
while(True):
    print("Player turn: ", Player)
    MoveRow = int(input("Please enter the row: "))
    MoveColumn = int(input("Please enter the column: "))
    if Player == 1:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            Player = 2
    else:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            Player = 1
    drawFields(currentField)
