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
        

def printGrid(grid:list,spaceGrid:list):
    
    os.system('cls')
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j]+spaceGrid[i][j], end="")
        print("\n")


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
        spaceGrid.append([])
        for k in range(len(grid[h])):
            spaceGrid[h].append(" "+(biggestLength-len(grid[h][k]))*" ")

    return spaceGrid


def is_same_grid(grid1, grid2) -> bool:
    
    if len(grid1)== len(grid2):
        
        lenGrid:int = len(grid1)
        
        for i in range(lenGrid):
            
            for j in range(len(grid1[i])):
                
                if grid1[i][j] != grid2[i][j]:
                    return False
                
        return True
    
    else:
        return False
            

def test():
    
    #test move right   
    grid = \
        [
            ["2", "□", "□", "□" ],
            ["2", "□", "□", "□" ],
            ["2", "□", "□", "□" ],
            ["2", "□", "□", "□" ],
        ]
    
    expected_result = \
        [
            ["□", "□", "□", "2" ],
            ["□", "□", "□", "2" ],
            ["□", "□", "□", "2" ],
            ["□", "□", "□", "2" ],
        ]
        
    grid,flag = move_right(grid)
    
    if is_same_grid(grid, expected_result):
        print("MOVE RIGHT SUCCESS")
    else:
        print("MOVE RIGHT FAILURE")
    
    
    #test move up   
    grid = \
        [
            ["□", "□", "□", "□" ],
            ["□", "□", "□", "□" ],
            ["□", "□", "□", "□" ],
            ["2", "2", "2", "2" ],
        ]
    
    expected_result = \
        [
            ["2", "2", "2", "2" ],
            ["□", "□", "□", "□" ],
            ["□", "□", "□", "□" ],
            ["□", "□", "□", "□" ],
        ]
        
    grid,flag = move_up(grid)
    
    if is_same_grid(grid, expected_result):
        print("MOVE UP SUCCESS")
    else:
        print("MOVE UP FAILURE")
    
    #test fusion   
    grid = \
        [
            ["□", "□", "□", "□" ],
            ["□", "□", "□", "□" ],
            ["16", "8", "4", "2" ],
            ["16", "8", "4", "2" ],
        ]
    
    expected_result = \
        [
            ["□", "□", "□", "□" ],
            ["□", "□", "□", "□" ],
            ["□", "□", "□", "□" ],
            ["32", "16", "8", "4" ],
        ]
        
    grid,flag = move_down(grid)
    
    if is_same_grid(grid, expected_result):
        print("FUSION SUCCESS")
    else:
        print("FUSION FAILURE")
    
    #test non fusion   
    grid = \
        [
            ["□", "□", "□", "□" ],
            ["□", "□", "□", "□" ],
            ["2", "8", "2", "4" ],
            ["16", "2", "4", "2" ],
        ]
    
    expected_result = \
        [
            ["□", "□", "□", "□" ],
            ["□", "□", "□", "□" ],
            ["2", "8", "2", "4" ],
            ["16", "2", "4", "2" ],
        ]
        
    grid,flag = move_down(grid)
    
    if is_same_grid(grid, expected_result):
        print("NON FUSION SUCCESS")
    else:
        print("NON FUSION FAILURE")

    #test fusion unique  
    grid = \
        [
            ["□", "□", "2", "□" ],
            ["2", "4", "2", "8" ],
            ["2", "4", "2", "8" ],
            ["2", "4", "2", "8" ],
        ]
    
    expected_result = \
        [
            ["□", "□", "□", "□" ],
            ["□", "□", "□", "□" ],
            ["2", "4", "4", "8" ],
            ["4", "8", "4", "16" ],
        ]
        
    grid,flag = move_down(grid)
    
    if is_same_grid(grid, expected_result):
        print("UNIQUE FUSION SUCCESS")
    else:
        print("UNIQUE FUSION FAILURE")



def jeu()->None:
        global grid
        grid=generateGrid()
        emptySlots=checkEmptySlots(grid)
        
        init(grid,emptySlots) 
        
        spaceGrid = alignGrid(grid)
        printGrid(grid,spaceGrid)
        valid_keys={"z", "s", "q", "d"}
        

        while True:
            key = keyboard.read_event(suppress=True)

            if key.event_type == keyboard.KEY_DOWN:
                if key.name in valid_keys:
                    if key.name == 'q':
                        grid, _ = move_left(grid)
                    elif key.name == 'd':
                        grid, _ = move_right(grid)
                    elif key.name == 'z':
                        grid, _ = move_up(grid)
                    elif key.name == 's':
                        grid, _ = move_down(grid)
                
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