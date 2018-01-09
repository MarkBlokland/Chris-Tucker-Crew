class car:
    direction = 'horizontal'
    position = []
    
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
if car2.position is in car3.position -> collision
car = car()
car.changeDirection()
print(car.direction)
'''

HEIGHT = None
WIDTH = None
RED_CAR_COORDINATE = 1
exit_coordinate = 'not initialized'
    
matrix = []
matrix.append([0,0,0,0])
matrix.append([0,RED_CAR_COORDINATE,RED_CAR_COORDINATE,2])
matrix.append([0,0,0,2])
matrix.append([0,0,0,0])

HEIGHT = len(matrix)
WIDTH = len(matrix[0])

for i in range(HEIGHT):
    for j in range(WIDTH):
        if exit_coordinate is 'not initialized' and matrix[i][j] == RED_CAR_COORDINATE:
            exit_coordinate = [i,WIDTH-1]
        
