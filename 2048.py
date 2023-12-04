import random
import os
from Tools import *

SIZE:int=4
grid:list=[]
emptySlots:list=[]

def generateGrid()->None:
    for i in range(SIZE):
        grid.append([])
        
        for j in range(SIZE):
            grid[i].append("□")

def checkEmptySlots()->None:
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j]=="□":
                emptySlots.append((i,j))
            
def getRandomPos()->int:
    return random.randint(0,len(emptySlots))

def randomGen():

    checkEmptySlots()
    randomPos:int = getRandomPos()
    
    if random.randint(1,10)<9:
        grid[emptySlots[randomPos][0]][emptySlots[randomPos][1]]="2"
    else:
        grid[emptySlots[randomPos][0]][emptySlots[randomPos][1]]="4"

def init():
    generateGrid()
    
    for i in range(2):
        randomGen()
        
def move(direction=str): 
    if direction=="up":
        pass
    
def printGrid():
    for i in grid:
        print(" ".join(i))
              
def jeu():
    
    init()
    printGrid()
    """while True:
        playMove:str= AskInputs("Choisissez une direction (z,q,s,d):", ["z","q","s","d"])
        if playMove=="z":
            move("up")"""

jeu()