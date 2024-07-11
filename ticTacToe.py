
grid = [["  "," ", " "],
        [" ", " ", " "],
        [" "," "," ",]]

#déclaration d'un tableau de tableau

def displayGrid(grid):
    for row in range (len(grid)):
        for column in range (len(grid[row])):
            print(grid[row][column],end="") #print ligne row et colonne column
            if (column != 2):
                print ("|",end="") #permet d'aller à la ligne
        print()

def gameIsNull(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column]==" ":
                return False
    return True

def gameIsWin(grid):
    for i in range (len(grid)) : 
        if grid [i][0] == grid[i][1] and grid[i][1] == grid[i][2] and grid[i][2] !=" ":
            return True
        if grid [0][i] == grid[1][i] and grid[1][i] == grid[2][i] and grid[2][i] !=" ":
            return True
    if grid [0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[2][2] !=" ":
        return True
    if grid [0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[2][0] !=" ":
        return True
    return False;

currentPlayer="X"
while not gameIsNull(grid) and not gameIsWin(grid) :
    row = int (input("select row : "))
    column = int (input ("select column : "))
    if grid[row][column] != " ":
        print("Play another case ! Please")
        continue
    grid[row][column] = currentPlayer
    displayGrid(grid)
    if not gameIsWin(grid) :
        if currentPlayer == "X" :
            currentPlayer ="O"
        else :
            currentPlayer="X"
    else : 
        print(currentPlayer, "is the winner!")

        
displayGrid(grid)