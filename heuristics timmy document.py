# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
hallo = [[0,1,0,3],
         [2,1,0,3],
         [2,0,4,4],
         [5,5,5,7],
         [6,0,8,7],
         [6,0,8,0],
         [6,0,8,0]]
         
board2 = [[0,0,2,2,3,3],
          [0,4,4,5,5,6],
          [0,0,1,1,7,6],
          [9,9,8,8,7,6],
          [10,0,0,11,12,12],
          [10,0,0,11,13,13]]

board3 = [[0,2,2,3,3,3],
          [0,4,4,5,6,6],
          [1,1,7,5,0,8],
          [9,9,7,10,10,8],
          [11,0,12,0,13,13],
          [11,0,12,0,0,0]]
          
board4 = [[2,3,3,3,0,4,0,0,0],
          [2,0,0,5,0,4,6,6,6],
          [0,0,0,5,0,4,0,0,9],
          [7,7,0,5,0,8,8,8,9],
          [10,1,1,11,0,0,0,0,9],
          [10,0,14,11,0,12,12,12,17],
          [13,13,14,15,16,16,0,0,17],
          [18,0,14,15,20,0,0,0,0],
          [18,19,19,19,20,21,21,22,22]]
          
board5 = [[2,2,2,3,0,4,5,0,0],
          [0,0,0,3,0,4,5,6,6],
          [0,0,0,3,7,7,8,0,0],
          [0,0,0,0,9,9,8,10,10],
          [0,0,11,11,11,12,1,1,13],
          [14,0,15,0,0,12,0,0,13],
          [14,0,15,16,16,12,17,17,13],
          [18,19,20,20,22,23,23,23,24],
          [18,19,21,21,22,0,0,0,24]]
          
board6 = [[2,2,3,3,4,0,0,5,0],
          [7,8,8,8,4,6,6,5,0],
          [7,0,9,9,10,11,0,12,12],
          [0,0,14,15,10,11,13,13,13],
          [1,1,14,15,0,0,0,0,0],
          [0,16,0,15,17,17,18,18,19],
          [20,16,21,21,22,23,23,23,19],
          [20,0,24,24,22,25,25,0,19],
          [20,26,26,26,22,0,0,0,0]]

board7 = [[2,0,0,0,0,0,3,4,4,4,5,5],
          [2,0,0,0,0,6,3,0,0,0,7,8],
          [9,9,9,10,10,6,11,12,12,0,7,8],
          [13,14,0,0,0,14,11,15,15,16,16,0],
          [13,14,17,17,17,14,11,18,18,18,0,0],
          [13,14,1,1,19,20,0,0,0,0,0,0],
          [21,21,21,23,19,20,25,26,0,27,28,28],
          [22,22,22,23,24,24,25,26,0,27,30,30],
          [31,31,32,33,33,33,25,34,34,34,0,35],
          [0,0,32,37,37,37,38,0,39,39,40,35],
          [0,0,0,0,0,0,38,0,0,41,40,36],
          [0,42,42,43,43,43,38,0,0,41,40,36],]


width = len(hallo[0])
heigth = len(hallo)

def scanRow(i):
    for j in range(width):
        value = hallo[i][j]
        if j+1 < width: nextValue = hallo[i][j+1] 
        else: nextValue = 0
        if j+2 < width: nextNextValue = hallo[i][j+2] 
        else: nextNextValue = 0
        if j-1 >= 0:
            previousValue = hallo[i][j-1]
        else: previousValue = 0        
    
        if value != 0:
            if value == nextValue:
                if value != previousValue:
                    if value == nextNextValue:
                        print(value, nextValue, nextNextValue)
                        #ay = car(value, length = 3)  
                    else: print(value, nextValue)
                        #ay = car(value, length = 2)  
               
def scanColumn(i):
    for j in range(heigth):
        value = hallo[j][i]
        if j+1 < heigth: nextValue = hallo[j+1][i]
        else: nextValue = 0
        if j+2 < heigth: nextNextValue = hallo[j+2][i]
        else: nextNextValue = 0
        if j-1 >= 0:
            previousValue = hallo[j-1][i]
        else: previousValue = 0
        
        if value != 0:
            if value == nextValue:
                if value != previousValue:
                    if value == nextNextValue:
                        print(value, nextValue, nextNextValue)
                        #ay = car(value, length = 3)
                    else: print(value, nextValue)
                        #ay = car(value, length = 2)
 
################ GET ALL CARS #####################
for i in range(width):
    scanColumn(i)
    
for i in range(heigth):
    scanRow(i)
    
################################################
