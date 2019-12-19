
#Create conditions for boats placement in grid (b needs to touch b while in same boat)
#Error Management/Restrictions





###Defenitions###

def createGrid(value):
    gridsize=value
    grid=[]
    for x in range(gridsize):
        temp=[]
        for y in range (gridsize):
            temp.append("W")
        grid.append(temp)
        
    return grid

def printGridWithoutHide(grid):
    for y in range (len(grid)+1):
        print (y, end = " ")
    print ("")
    for x in range (len(grid)):
        print (x+1, end = " ")
        for y in range (len(grid)):
            print (grid[x][y], end = " ")
        print("")
        


def printGrid(grid):
    for y in range (len(grid)+1):
        print (y, end = " ")
    print ("")
    for x in range (len(grid)):
        print (x+1, end = " ")
        for y in range (len(grid)): ####Hide B value when printing####
            if(grid[x][y] == "B"):
                print("W", end = " ")
            else:
                print (grid[x][y], end = " ")
                
        print("")
    
        
def placeBoat(grid, boatcount):
    count=1
    while(count<=boatcount):
        boatsize=count+1
        print("Place boat " + str(count) + " of length " + str(boatsize) + "!")
        x=input ("Enter X coord: ")
        x=int(x)-1
        y=input ("Enter Y coord: ")
        y=int(y)-1
        direction=input ("Enter direction (N, E, S, W): ")
        direction=direction.strip()
        
        try:
            for b in range(boatsize):
                grid[y][x]="B"
                if direction.lower() == "n":
                    y-=1
                elif direction.lower() == "e":
                    x+=1
                elif direction.lower() == "s":
                    y+=1
                elif direction.lower() == "w":
                    x-=1
            count+=1
            printGridWithoutHide(grid)
            
        except:
            print ("Invalid boat placement")
        
        
            
    return grid

        
       


def startGame():
    print ("")
    print ("!!!BATTLESHIP!!!"+"\n")
    print ("Press Enter to start!.")
    input ("")




def attack(defender):
    print("ATTACK!")
    x=input ("Enter X coord: ")
    y=input ("Enter Y coord: ")
    x=int(x)-1
    y=int(y)-1
    print (defender[y][x])
    if defender[y][x]=="B":
        print ("Hit")
        defender[y][x]="H"
    else:
        print ("Miss")
        defender[y][x]="M"
    
    return defender



def isAlive(grid):
    Alive=False
    for x in grid:
        for y in x:
            if y=="B":
                Alive=True

    return Alive




            
        
###Start Game###
p1=("\nPlayer 1, its your turn!\nPress Enter to continue.")
p2=("\nPlayer 2, its your turn!\nPress Enter to continue.")

startGame()

gridDim=input("Please select Grid dimension: ")

player1Grid=createGrid(int(gridDim))
if (len(player1Grid)<=10):
    boatQts=2
elif (len(player1Grid)>15):
    boatQts=4
else:
    boatQts=3

print("You will play with " + str(boatQts) + " boats!")

###Place Boats - Player1###
print(p1)
input("")
printGridWithoutHide(player1Grid)
player1Grid=placeBoat(player1Grid, boatQts)
input("")



###Place Boats - Player2###
player2Grid=createGrid(int(gridDim))
print(p2)
input("")
printGridWithoutHide(player2Grid)
player2Grid=placeBoat(player2Grid, boatQts)
input("")



###Attack Loop###
while (True):
    print(p1)
    input("")
    printGrid(player2Grid)
    attack(player2Grid)
    if (not isAlive(player2Grid)):
        print("Boat as been Sink! Player1 Won!")
        break

    print(p2)
    input("")
    printGrid(player1Grid)
    attack(player1Grid)
    if (not isAlive(player1Grid)):
        print("Boat as been Sink! Player2 Won!")
        break
    

    

