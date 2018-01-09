WIDTH = 6
HEIGHT = 6

matrix = []
matrix.append([0,0])
matrix.append([1,0])

def a(x):
    x.append([1,1])
    print(len(x))
    
print(matrix)

cars_checked = []
        
def recursion(current_car, target_coordinate):
    if current_car in cars_checked:
        return
        
    if current_car.direction == 'horizontal':
        ###################### checking right ##############################
        x = current_car.head[0]
        y = current_car.head[1]

        if x + 1 >= WIDTH:
            return
        
        while matrix[x+1][y] == 0: 
            current_car.head = [x+1,y]
            current_car.tail = [current_car.tail[0]+1, y]
            matrix[x+1][y] = current_car.number
            matrix[current_car.tail[0]-1][y] = 0
            x = x + 1
            if matrix[target_coordinate[0]][target_coordinate[1]] == 0:
                return
            
        cars_checked.append(current_car.number)
        current_car = return_car_object(matrix[x+1][y])
        recursion(current_car)
        
        if matrix[x+1][y] == 0:
            current_car.head = [x+1,y]
            current_car.tail = [current_car.tail[0]+1, y]
            matrix[x+1][y] = current_car.number
            matrix[current_car.tail[0]-1][y] = 0
        
        else: 
            ###################### checking left ##############################
            x = current_car.head[0]
            y = current_car.head[1]
            
            if x == 0:
                return
    
            while matrix[x-1][y] == 0:
                current_car.tail = [x-1,y]
                current_car.head = [current_car.head[0]-1, y]
                matrix[x-1][y] = current_car.number
                matrix[current_car.head[0]+1][y] = 0
                x = x - 1
                if matrix[target_coordinate[0]][target_coordinate[1]] == 0:
                    return
            
            cars_checked.append(current_car.number)
            current_car = return_car_object(matrix[x-1][y])
            recursion(current_car)
            if matrix[x-1][y] == 0:
                current_car.tail = [x-1,y]
                current_car.head = [current_car.head[0]-1, y]
                matrix[x-1][y] = current_car.number
                matrix[current_car.head[0]+1][y] = 0
        
    else:
        ###################### checking above ##############################
        x = current_car.head[0]
        y = current_car.head[1]

        if y + 1 >= HEIGHT:
            return

        while matrix[x][y+1] == 0:
            current_car.head = [x, y+1]
            current_car.tail = [x, current_car.tail[1]+1]
            matrix[x][y+1] = current_car.number
            matrix[x][current_car.tail[1]-1] = 0
            y = y + 1
            if matrix[target_coordinate[0]][target_coordinate[1]] == 0:
                return
            
        cars_checked.append(current_car.number)
        current_car = return_car_object(matrix[x][y+1])
        recursion(current_car)
           
        if matrix[x][y+1] == 0:
            current_car.head = [x, y+1]
            current_car.tail = [x, current_car.tail[1]+1]
            matrix[x][y+1] = current_car.number
            matrix[x][current_car.tail[1]-1] = 0  
        else:
            ###################### checking below ##############################    
            x = current_car.head[0]
            y = current_car.head[1]
            
            if x == 0:
                return            
            
            while matrix[x][y-1] == 0:
                current_car.head = [x, y-1]
                current_car.tail = [x, current_car.tail[1]-1]
                matrix[x][y-1] = current_car.number
                matrix[x][current_car.tail[1]+1] = 0
                y = y - 1
                if matrix[target_coordinate[0]][target_coordinate[1]] == 0:
                    return
                
            cars_checked.append(current_car.number)
            current_car = return_car_object(matrix[x][y-1])
            recursion(current_car)
            
            if matrix[x][y-1] == 0:
                current_car.head = [x, y-1]
                current_car.tail = [x, current_car.tail[1]-1]
                matrix[x][y-1] = current_car.number
                matrix[x][current_car.tail[1]+1] = 0
    
    
recursion(red_car)