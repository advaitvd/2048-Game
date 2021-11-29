
import numpy as np

class Grid:
    def __init__(self,n):
        self.matrix=np.zeros((n,n),dtype=int)
        self.matrix[np.random.randint(n),np.random.randint(n)]=2*np.random.randint(1,3)
        self.matrix[np.random.randint(n),np.random.randint(n)]=2*np.random.randint(1,3)
    
    def display_grid(self):
        
        for i in range(len(self.matrix)):
            
            print('+------'*len(self.matrix),end='+\n')
            print('| ',end='')
            
            for j in range(len(self.matrix)):
                print(f'{self.matrix[i,j]:>4}',end=' | ')
            
            print()
        
        print('+------'*len(self.matrix),end='+\n')
        


def run():
    grid=Grid(4)
    grid.matrix[0,0]=2048
    grid.display_grid()

if __name__ == "__main__":
    run()
    # print(np.random.randint(6))