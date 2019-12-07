#### DAY THREE ####
import itertools

WIRE_ONE = 0
WIRE_TWO = 1


def readingInput():
    print("Get the puzzle input")
    lineReadForList = [] 
    puzzleInputFile = open("puzzle_input.txt","r")
    #read line by line
    line = puzzleInputFile.readlines()
    for readline in line:
        lineReadForList.append(readline.split(",")) 
    #close file
    puzzleInputFile.close()
    #ordered the list in two dimension with format [direction,number of point in this direction]   
    for i in range(len(lineReadForList)):
        for a in range(len(lineReadForList[i])):
            lineReadForList[i][a] = [ str(lineReadForList[i][a][:1]),int(lineReadForList[i][a][1:])]
    return lineReadForList



direction = readingInput()
segFirstWire = []#[x1;y1]
segSecondWire = []#[x2;y2]
segFirstWire.append([0,0])
segSecondWire.append([0,0])
listDroiteFirstWire = []#[a1;b1]
listDroiteSecondWire = []#[a2;b2]

print("get segment from wire one")
indexX = 0         
indexY = 0 
for i in range(len(direction[WIRE_ONE])):
     if(direction[WIRE_ONE][i][0] == 'R'):
         segFirstWire.append([ indexX + direction[WIRE_ONE][i][1] , indexY  ])
         indexX = indexX + direction[WIRE_ONE][i][1]
     elif(direction[WIRE_ONE][i][0] == 'L'): 
         segFirstWire.append([ indexX - direction[WIRE_ONE][i][1] , indexY  ])
         indexX = indexX - direction[WIRE_ONE][i][1]
     elif(direction[WIRE_ONE][i][0] == 'U'):
         segFirstWire.append([ indexX , indexY + direction[WIRE_ONE][i][1] ])
         indexY = indexY + direction[WIRE_ONE][i][1]
     elif(direction[WIRE_ONE][i][0] == 'D'): 
         segFirstWire.append([ indexX , indexY - direction[WIRE_ONE][i][1] ])
         indexY = indexY - direction[WIRE_ONE][i][1]
     else:
         print("NO MORE DIRECTION")
         break

print("get segment from wire two")
indexX = 0
indexY = 0
for i in range(len(direction[WIRE_TWO])):
     if(direction[WIRE_TWO][i][0] == 'R'):
         segSecondWire.append([ indexX + direction[WIRE_TWO][i][1] , indexY  ])
         indexX = indexX + direction[WIRE_TWO][i][1]
     elif(direction[WIRE_TWO][i][0] == 'L'): 
         segSecondWire.append([ indexX - direction[WIRE_TWO][i][1] , indexY  ])
         indexX = indexX - direction[WIRE_TWO][i][1]
     elif(direction[WIRE_TWO][i][0] == 'U'):
         segSecondWire.append([ indexX , indexY + direction[WIRE_TWO][i][1] ])
         indexY = indexY + direction[WIRE_TWO][i][1]
     elif(direction[WIRE_TWO][i][0] == 'D'): 
         segSecondWire.append([ indexX , indexY - direction[WIRE_TWO][i][1] ])
         indexY = indexY - direction[WIRE_TWO][i][1]
     else:
         print("NO MORE DIRECTION")
         break

print("SEARCH result")
result = []
print str(len(segFirstWire))
print segFirstWire
print segSecondWire



