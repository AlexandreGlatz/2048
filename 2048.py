import random
import os
from Tools import *

SIZE:int=4
emptySlots:list=[]

#génére grille de jeu
def generateGrid()->list:
    grid:list=[]
    '''génère la grille ->None'''
    for i in range(SIZE):
        grid.append([])
        
        for j in range(SIZE):
            grid[i].append("□")

    return grid


def checkEmptySlots(grid:list)->None:
    emptySlots.clear()
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j]=="□":
                emptySlots.append((i,j))

def getRandomPos()->int:
    '''permet d'avoir une position random ->int '''
    return random.randint(0,len(emptySlots)-1)

def randomGen(grid:list)->None:
    '''#générer les 2 et les 4'''
    randomPos:int = getRandomPos()
    
    if random.randint(1,10)<9:
        grid[emptySlots[randomPos][0]][emptySlots[randomPos][1]]="2"
    else:
        grid[emptySlots[randomPos][0]][emptySlots[randomPos][1]]="4"


def init()->list:
    '''#permet d'init le jeu'''
    grid = generateGrid()
    
    for i in range(2):
        randomGen(grid)
    
    return grid

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
        

def printGrid(grid:list):
    
    os.system('cls')
    
    for i in grid:
        print(" ".join(i))

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


def jeu():
    while True:
        grid = init()

        printGrid(grid)

        while True:
            grid = move(grid)
            state = gameStateWin(grid)
            
            if gameStateWin(grid) == 'Continuez à jouer !':
                
                if len(emptySlots) - 1 > 0:
                    randomGen(grid)

            if gameStateWin(grid) == 'Perdu D:':
                print("Vous avez perdu !")
                if not Retry():
                    return

            printGrid(grid)
            print(state)

            
        
        
        

jeu()