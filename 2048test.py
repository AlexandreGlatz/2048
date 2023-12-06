import random
import os
from Tools import *
import keyboard

SIZE: int = 4



def generateGrid() -> list:
    grid: list = []
    for i in range(SIZE):
        grid.append([])
        for j in range(SIZE):
            grid[i].append("□")
    return grid


def checkEmptySlots(grid: list) -> None:
    emptySlots: list = []
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == "□":
                emptySlots.append((i, j))
    return emptySlots


def getRandomPos(emptySlots:list) -> int:
    return random.randint(0, len(emptySlots) - 1)


def randomGen(grid: list, emptySlots:list) -> None:
    checkEmptySlots(grid)
    randomPos: int = getRandomPos(emptySlots)
    if random.randint(1, 10) < 9:
        grid[emptySlots[randomPos][0]][emptySlots[randomPos][1]] = "2"
    else:
        grid[emptySlots[randomPos][0]][emptySlots[randomPos][1]] = "4"


def init(grid:list,emptySlots:list) -> None:
    for i in range(2):
        randomGen(grid, emptySlots)

def compress(grid:list):

    changed = False
    new_grid = generateGrid()  
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != "□":
                new_grid[i][pos] = grid[i][j]
                if j != pos:
                    changed = True
                pos += 1

    return new_grid, changed

def merge(grid:list):
     
    changed = False
     
    for i in range(4):
        for j in range(3):
            if(grid[i][j] == grid[i][j + 1] and grid[i][j] != "□"):

                grid[i][j] = str(int(grid[i][j]) * 2)
                grid[i][j + 1] = "□"

                changed = True
 
    return grid, changed

def reverse(grid:list):
    
    new_grid =[]
    
    for i in range(4):
        new_grid.append([])
        
        for j in range(4):
            new_grid[i].append(grid[i][3 - j])
            
    return new_grid

def transpose(grid:list):

    new_grid = []
    for i in range(4):
        new_grid.append([])

        for j in range(4):
            new_grid[i].append(grid[j][i])
            
    return new_grid
    
def move_left(grid:list):
	new_grid, changed1 = compress(grid)

	new_grid, changed2 = merge(new_grid)
	
	changed = changed1 or changed2

	new_grid, temp = compress(new_grid)

	return new_grid, changed



def move_right(grid:list):

 
	new_grid = reverse(grid)


	new_grid, changed = move_left(new_grid)


	new_grid = reverse(new_grid)


	return new_grid, changed

    
def move_up(grid:list):


	new_grid = transpose(grid)


	new_grid, changed = move_left(new_grid)


	new_grid = transpose(new_grid)
	return new_grid, changed


def move_down(grid:list):

	new_grid = transpose(grid)

	new_grid, changed = move_right(new_grid)


	new_grid = transpose(new_grid)
	return new_grid, changed


def move(grid)->list:
    
    playerInput = AskInputs("Quel mouvement voulez-vous faire ? (z,q,s,d): ", ["z","q","s","d"])
    
    if playerInput =="q":

        grid, _ = move_left(grid)
        
    elif playerInput =="d":

        grid, _ =move_right(grid)
        
    elif playerInput =="z":   
        
        grid, _ =move_up(grid)
    
    elif playerInput =="s":

        grid, _ =move_down(grid)

    return grid
        

def printGrid(grid:list,spaceGrid:list):
    
    #os.system('cls')
    
    for i in range(len(grid)):
        print(space
              Grid[i].join(grid[i]))

def gameStateWin(grid: list) -> str:
    
    for i in range(4):
        for j in range(4):
            if grid[i][j] != "□":
                if int(grid[i][j]) == 2048:
                    return 'Gagné !'

    for i in range(4):
        for j in range(4):
            if grid[i][j] == "□":
                return 'Continuez à jouer !'

    for i in range(3):
        for j in range(3):
            if grid[i][j] != "□":
                if int(grid[i][j]) == int(grid[i + 1][j]) or int(grid[i][j]) == int(grid[i][j + 1]):
                    return 'Continuez à jouer !'

    return 'Perdu D:'

def alignGrid(grid: list) -> list:
    biggestLength = 0
    spaceGrid=[]
    for i in range(len(grid)):
        for j in grid[i]:
            if len(j)>biggestLength:
                biggestLength = len(j)
    
    for h in range(len(grid)):
        for k in range(len(grid[h])):
            spaceGrid.append((biggestLength-len(grid[h][k]))*"a")

    
    print(spaceGrid)
    return spaceGrid



def jeu()->None:
    
        grid = generateGrid()
        emptySlots=checkEmptySlots(grid)
        
        init(grid,emptySlots) 
        
        spaceGrid = alignGrid(grid)
        printGrid(grid,spaceGrid)

        while True:
            emptySlots=checkEmptySlots(grid)
            grid = move(grid)
            emptySlots=checkEmptySlots(grid)
            spaceGrid = alignGrid(grid)
            state = gameStateWin(grid)
            
            if gameStateWin(grid) == 'Continuez à jouer !':
                
                if len(emptySlots) > 0:
                    randomGen(grid,emptySlots)

            if gameStateWin(grid) == 'Perdu D:':
                printGrid(grid,spaceGrid)
                print("Vous avez perdu !")
                if not Retry():
                    return
                else:
                    grid = generateGrid()
                    emptySlots=checkEmptySlots(grid)
                    init(grid,emptySlots) 
            
            if gameStateWin(grid) == 'Gagné !':
                printGrid(grid,spaceGrid)
                print("Vous avez Gagné !! gg")
                if not Retry():
                    return
                else:
                    grid = generateGrid()
                    emptySlots=checkEmptySlots(grid)
                    init(grid,emptySlots) 

            printGrid(grid,spaceGrid)
            print(state)

            
        
        
        

jeu()