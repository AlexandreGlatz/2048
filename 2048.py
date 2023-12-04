import random 

WIDTH:int=4
HEIGHT:int=4

def generateGrid()->list:
    grid:list=[]
    emptySlots:list=[]
    
    for i in range(WIDTH):
        grid.append([])
        grid.append([])
        
        for j in range(HEIGHT):
            grid[i].append("")
            grid[i].append((i,j))
            
    return grid, emptySlots

def popSlot(emptySlots,index):
    emptySlots[index]=emptySlots[-1]
    emptySlots.pop()
    return emptySlots
    
def getRandomPos(emptySlots)->int:
    return random.randint(len(emptySlots))

def randomGen(grid,emptySlots):
    
    for i in range(2):
    
        randomPos:int = getRandomPos()
        popSlot(getRandomPos)
        
        if random.randint(1,10)<9:
            grid[emptySlots[randomPos[0]]][emptySlots[randomPos[1]]]=2
        else:
            grid[emptySlots[randomPos[0]]][emptySlots[randomPos[1]]]=4

def jouer():
    
    grid,emptySlots = generateGrid()
        