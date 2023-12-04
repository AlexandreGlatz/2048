import random
import os

SIZE:int=4
grid:list=[]
emptySlots:list=[]

def generateGrid()->None:
    for i in range(SIZE):
        grid.append([])
        
        for j in range(SIZE):
            grid[i].append("")

def checkEmptySlots()->None:
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j]=="":
                emptySlots.append((i,j))
            
def getRandomPos()->int:
    return random.randint(0,len(emptySlots))

def randomGen():

    checkEmptySlots()
    randomPos:int = getRandomPos()
    
    if random.randint(1,10)<9:
        grid[emptySlots[randomPos][0]][emptySlots[randomPos][1]]=2
    else:
        grid[emptySlots[randomPos][0]][emptySlots[randomPos][1]]=4

def init():
    generateGrid()
    
    for i in range(2):
        randomGen()
    
def jeu():
    
    init()
    while True:
        

jeu()