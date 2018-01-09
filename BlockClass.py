import numpy as numpy

class Block:  
    
    def __init__(self, tail, head, direction):
        self.tail = tail
        self.head = head
        self.direction = direction
     
    def initialize(self,head,tail,constant,direction):
        self.head = head
        self.tail = tail
        self.constant = constant
        self.direction = direction

board = numpy.array([[0,0,5,3,3,2],
                    [0,0,5,0,0,2],
                    [0,0,5,1,1,2],
                    [0,0,0,6,4,4],
                    [9,8,8,6,0,0],
                    [9,0,0,6,10,10]])

def extractCars(board):
    def checkRight(i,j,carNumber,length):
        if j < maxVerti: # Dont go outside the board...
            if board[i,j] == carNumber: # Does this tile contain a part of car -carNumber-
                length = length + 1 #If so, its length is bigger than previously thought
                return checkRight(i,j+1,carNumber,length) # Are there more parts to the right?
        return length #Returns the total length of the car found
    
    def checkUnder(i,j,carNumber,length):
        if i < maxHori: 
            if board[i,j] == carNumber:
                length = length + 1
                return checkUnder(i+1,j,carNumber,length) 
        return length
    
    carsAll = dict()
    maxHori, maxVerti = len(board), len(board[0])
    carsDone = [0] #Contains the carNumbers that have already been classed
    for j in range(maxVerti):
        for i in range(maxHori):
            if board[i,j] not in carsDone: 
                carNumber = board[i,j] 
                tailCoord = [i,j]
                length = checkRight(i,j+1,carNumber,1)
                if length != 1: #If true then car is horizontal
                    headCoord = [i,j+length-1]
                    carsAll[carNumber] = Block(tailCoord, headCoord, 'horizontal')
                else: #Car is vertical
                    headCoord = [i+checkUnder(i+1,j,carNumber,1)-1,j]
                    carsAll[carNumber] = Block(tailCoord, headCoord, 'vertical')
                carsDone.append(carNumber) #So we dont check the same car again      
                
    return carsAll

carsCatalogod = extractCars(board)



#The dictionary / hashmap!!!

streetno = { "1": a} #Create dictionary
streetno["1"].head
streetno["2"] = a
streetno["1"].head
streetno = dict()
ko = 5
streetno["2"] = Block(5,5,'ver')
streetno["1"] = a
streetno["1"].head
