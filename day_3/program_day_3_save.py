#### DAY THREE ####
import itertools

WIRE_ONE = 0
WIRE_TWO = 1

ABSISE = 0
ORDONNE = 1

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
movingPoint = []
segFirstWire = []
segSecondWire = []
movingPoint.append([[0],[0]])
segFirstWire.append([0,0])
segSecondWire.append([0,0])
mon_tuple= ()
indexX = 0         
indexY = 0 
for i in range(len(direction[WIRE_ONE])):
     if(direction[WIRE_ONE][i][0] == 'R'):
         for a in range(direction[WIRE_ONE][i][1]):
              mon_tuple = (indexX + (a+1 ), indexY)
              segFirstWire.append(mon_tuple)
         indexX = indexX + direction[WIRE_ONE][i][1]
     elif(direction[WIRE_ONE][i][0] == 'L'): 
         for a in range(direction[WIRE_ONE][i][1]):
              mon_tuple = (indexX - (a+1 ), indexY)
              segFirstWire.append(mon_tuple)
         indexX = indexX - direction[WIRE_ONE][i][1]
     elif(direction[WIRE_ONE][i][0] == 'U'):
         for a in range(direction[WIRE_ONE][i][1]):
              mon_tuple = (indexX , indexY+(a+1)
              segFirstWire.append(mon_tuple)
         indexY = indexY + direction[WIRE_ONE][i][1]
     elif(direction[WIRE_ONE][i][0] == 'D'): 
         for a in range(direction[WIRE_ONE][i][1]):
              mon_tuple = (indexX , indexY-(a+1))
              segFirstWire.append(mon_tuple)
         indexY = indexY - direction[WIRE_ONE][i][1]
     else:
         print("NO MORE DIRECTION")
         break
indexX = 0
indexY = 0
for i in range(len(direction[WIRE_TWO])):
     if(direction[WIRE_TWO][i][0] == 'R'):
         for a in range(direction[WIRE_TWO][i][1]):
              segSecondWire.append([ indexX + (a+1) , indexY  ])
         indexX = indexX + direction[WIRE_TWO][i][1]
     elif(direction[WIRE_TWO][i][0] == 'L'):
         for a in range(direction[WIRE_TWO][i][1]):
              segSecondWire.append([ indexX - (a+1) , indexY  ])
         indexX = indexX - direction[WIRE_TWO][i][1]

     elif(direction[WIRE_TWO][i][0] == 'U'):
         for a in range(direction[WIRE_TWO][i][1]):
              segSecondWire.append([ indexX , indexY + (a+1) ])
         indexY = indexY + direction[WIRE_TWO][i][1]
     elif(direction[WIRE_TWO][i][0] == 'D'):
         for a in range(direction[WIRE_TWO][i][1]):
              segSecondWire.append([ indexX , indexY - (a+1) ])
         indexY = indexY - direction[WIRE_TWO][i][1]
     else:
         print("NO MORE DIRECTION")
         break
print("SEARCH result")
result = []
#print str(len(segFirstWire))
#for x in range(len(segFirstWire)):
#    print x
#    if( ( segFirstWire[x][0] != 0 ) and ( segFirstWire[x][1] != 0 )):
#        if segFirstWire[x] in segSecondWire:
#            print "yes"
#            print segFirstWire[x]
#            result.append(abs(segFirstWire[x][0]) + abs(segFirstWire[x][1]))

print segFirstWire 
print str(set(segFirstWire))



print result
print min(result)

####first result 
#[399, 600, 1122, 1139, 596, 511, 404, 293]
#293




