WIDTH = 6
HEIGHT = 6

cars_checked = []
        
def recursion(current_car, target_coordinate):
    if current_car in cars_checked:
        return
        
    if current_car.direction == 'horizontal':
        ###################### checking right ##############################
        y = current_car.head[1]
        if current_car.head[0]  + 1 >= WIDTH:
            return
        
        while matrix[current_car.head[0]+1][y] == 0: 
            current_car.head = [current_car.head[0]+1,y]
            current_car.tail = [current_car.tail[0]+1,y]
            matrix[current_car.tail[0]][y] = current_car.number
            matrix[current_car.tail[0]-1][y] = 0
            if matrix[target_coordinate[0]][target_coordinate[1]] == 0:
                return
            
        cars_checked.append(current_car.number)
        current_car = return_car_object(matrix[x+1][y])
        recursion(current_car, [current_car.head[0]+1,y])
        
        if matrix[current_car.head[0]+1][y] == 0: 
            current_car.head = [current_car.head[0]+1,y]
            current_car.tail = [current_car.tail[0]+1,y]
            matrix[current_car.tail[0]][y] = current_car.number
            matrix[current_car.tail[0]-1][y] = 0
        
        else: 
            ###################### checking left ##############################
            y = current_car.head[1]   
            if current_car.tail[0] == 0:
                return
    
            while matrix[current_car.tail[0]-1][y] == 0:
                current_car.tail = [current_car.tail[0]-1,y]
                current_car.head = [current_car.head[0]-1,y]
                matrix[current_car.tail[0]][y] = current_car.number
                matrix[current_car.head[0]+1][y] = 0
                if matrix[target_coordinate[0]][target_coordinate[1]] == 0:
                    return
            
            cars_checked.append(current_car.number)
            current_car = return_car_object(matrix[x-1][y])
            recursion(current_car, [current_car.tail[0]-1,y])
        
            if matrix[current_car.tail[0]-1][y] == 0:
                current_car.tail = [current_car.tail[0]-1,y]
                current_car.head = [current_car.head[0]-1,y]
                matrix[current_car.tail[0]][y] = current_car.number
                matrix[current_car.head[0]+1][y] = 0
        
    else:
        ###################### checking above ##############################
        x = current_car.head[0]
        
        if current_car.head[1] + 1 >= HEIGHT:
            return

        while matrix[x][current_car.head[1]+1] == 0:
            current_car.head = [x, current_car.head[1]+1]
            current_car.tail = [x, current_car.tail[1]+1]
            matrix[x][current_car.head[1]] = current_car.number
            matrix[x][current_car.tail[1]-1] = 0
            if matrix[target_coordinate[0]][target_coordinate[1]] == 0:
                return
            
        cars_checked.append(current_car.number)
        current_car = return_car_object(matrix[x][current_car.head[1]+1])
        recursion(current_car, [current_car.head[1]+1,y])
           
        if matrix[x][current_car.head[1]+1] == 0:
            current_car.head = [x, current_car.head[1]+1]
            current_car.tail = [x, current_car.tail[1]+1]
            matrix[x][current_car.head[1]] = current_car.number
            matrix[x][current_car.tail[1]-1] = 0
        else:
            ###################### checking below ##############################    
            x = current_car.head[0]
            
            if current_car.tail[1] == 0:
                return            
            
            while matrix[x][current_car.tail[1]-1] == 0:
                current_car.head = [x, current_car.head[1]-1]
                current_car.tail = [x, current_car.tail[1]-1]
                matrix[x][current_car.tail[1]] = current_car.number
                matrix[x][current_car.tail[1]+1] = 0
                if matrix[target_coordinate[0]][target_coordinate[1]] == 0:
                    return
                
            cars_checked.append(current_car.number)
            current_car = return_car_object(matrix[x][y-1])
            recursion(current_car, [current_car.head[1]-1,y])
            
            if matrix[x][current_car.tail[1]-1] == 0:
                current_car.head = [x, current_car.head[1]-1]
                current_car.tail = [x, current_car.tail[1]-1]
                matrix[x][current_car.tail[1]] = current_car.number
                matrix[x][current_car.tail[1]+1] = 0
    
    
recursion(red_car)
