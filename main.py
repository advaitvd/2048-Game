import numpy as np
import functools

GRID_SIZE=4
WIN_SCORE=2048

class Grid:
    def __init__(self,n):
        self.matrix=np.zeros((n,n),dtype=int)
        self.matrix[np.random.randint(n),np.random.randint(n)]=2*np.random.randint(1,3)
        self.matrix[np.random.randint(n),np.random.randint(n)]=2*np.random.randint(1,3)
    
    def display_grid(self):
        
        for i in range(GRID_SIZE):
            
            print('+------'*GRID_SIZE,end='+\n')
            print('| ',end='')
            
            for j in range(GRID_SIZE):
                print(f'{self.matrix[i,j]:>4}',end=' | ')
            
            print()
        
        print('+------'*GRID_SIZE,end='+\n')

    def left(self):
        for i in range(GRID_SIZE):
            non_zero_terms=self.matrix[i][self.matrix[i]>0]
            self.matrix[i,:]=0
            idx=0
            j=0
            while idx<len(non_zero_terms):
                if idx+1<len(non_zero_terms) and non_zero_terms[idx]==non_zero_terms[idx+1]:
                    self.matrix[i,j]=non_zero_terms[idx]+non_zero_terms[idx+1]
                    j+=1
                    idx+=2
                else:
                    self.matrix[i,j]=non_zero_terms[idx]
                    idx+=1
                    j+=1

    
    def right(self):
        for i in range(GRID_SIZE):
            non_zero_terms=self.matrix[i][self.matrix[i]>0]
            self.matrix[i,:]=0
            idx=len(non_zero_terms)-1
            j=GRID_SIZE-1
            while idx>=0:
                if idx-1>=0 and non_zero_terms[idx]==non_zero_terms[idx-1]:
                    self.matrix[i,j]=non_zero_terms[idx]+non_zero_terms[idx-1]
                    j-=1
                    idx-=2
                else:
                    self.matrix[i,j]=non_zero_terms[idx]
                    idx-=1
                    j-=1

    
    def up(self):
        for i in range(GRID_SIZE):
            non_zero_terms=self.matrix[:,i][self.matrix[:,i]>0]
            self.matrix[:,i]=0
            idx=0
            j=0
            while idx<len(non_zero_terms):
                if idx+1<len(non_zero_terms) and non_zero_terms[idx]==non_zero_terms[idx+1]:
                    self.matrix[j,i]=non_zero_terms[idx]+non_zero_terms[idx+1]
                    j+=1
                    idx+=2
                else:
                    self.matrix[j,i]=non_zero_terms[idx]
                    idx+=1
                    j+=1
    
    def down(self):
        for i in range(GRID_SIZE):
            non_zero_terms=self.matrix[:,i][self.matrix[:,i]>0]
            self.matrix[:,i]=0
            idx=len(non_zero_terms)-1
            j=GRID_SIZE-1
            while idx>=0:
                if idx-1>=0 and non_zero_terms[idx]==non_zero_terms[idx-1]:
                    self.matrix[j,i]=non_zero_terms[idx]+non_zero_terms[idx-1]
                    j-=1
                    idx-=2
                else:
                    self.matrix[j,i]=non_zero_terms[idx]
                    idx-=1
                    j-=1

    def find_empty_locations(self):
        empty_locations=[]
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.matrix[i,j]==0:
                    empty_locations.append((i,j))
        return empty_locations

    def fill_empty_location(self):
        empty_locations=self.find_empty_locations()
        if len(empty_locations)==0:
            return
        loc_to_fill=empty_locations[np.random.randint(len(empty_locations))]
        self.matrix[loc_to_fill[0],loc_to_fill[1]]=2*np.random.randint(1,3)

    def max_elem(self):
        return np.max(self.matrix)
        

def game_over(grid):
    for i in range(GRID_SIZE-1):
        for j in range(GRID_SIZE-1):
            if grid.matrix[i,j]==grid.matrix[i,j+1] or grid.matrix[i,j]==grid.matrix[i+1,j] or grid.matrix[i,j]==0:
                return False
    
    for i in range (GRID_SIZE-1):
        if grid.matrix[i,GRID_SIZE-1]==grid.matrix[i+1,GRID_SIZE-1] or grid.matrix[GRID_SIZE-1,i]==grid.matrix[GRID_SIZE-1,i+1] or grid.matrix[GRID_SIZE-1,i]==0 or grid.matrix[i,GRID_SIZE-1]==0:
            return False
    if grid.matrix[GRID_SIZE-1,GRID_SIZE-1]==0:
        return False
    return True

def run():
    grid=Grid(GRID_SIZE)
    while True:
        grid.display_grid()
        add_dir=int('0'+input("Enter a direction:\n >1 for left\n >2 for right\n >3 for up \n >4 for down\n$"))
        if add_dir==1:
            grid.left()
        elif add_dir==2:
            grid.right()
        elif add_dir==3:
            grid.up()
        elif add_dir==4:
            grid.down()
        else:
            print('Invalid input')
            continue
        
        if game_over(grid)==False:
            grid.fill_empty_location()
        else:
            if grid.max_elem()==WIN_SCORE:
                print('Congratulations! You acheived the winning score.')
            else:
                print('Game Over! Try again...')
            break

if __name__ == "__main__":
    run()
    # print(np.random.randint(6))