class car:
    direction = 'horizontal'
    head = [0,0]
    tail = [0,0]
    
    def changeDirection(self):
        if self.direction is 'horizontal':
            self.direction = 'vertical'
        else:
            self.direction = 'horizontal'
      
    def collision(Car):
        if ....:
            return true
        else:
            return false
        
        
        
'''
car = car()
car.changeDirection()
print(car.direction)
'''

HEIGHT = None
WIDTH = None
RED_CAR = 1
exit_coordinate = 'not initialized'
    
matrix = []
matrix.append([0,0,0,0])
matrix.append([0,RED_CAR,RED_CAR,2])
matrix.append([0,0,0,2])
matrix.append([0,0,0,0])

HEIGHT = len(matrix)
WIDTH = len(matrix[0])

for i in range(HEIGHT):
    for j in range(WIDTH):
        if exit_coordinate is 'not initialized' and matrix[i][j] == RED_CAR:
            exit_coordinate = [i,WIDTH-1]
        
