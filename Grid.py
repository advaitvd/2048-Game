import numpy as np

class Grid:
    GRID_SIZE=4
    WIN_SCORE=2048
    def __init__(self,n):
        self.matrix=np.zeros((n,n),dtype=int)
        self.matrix[np.random.randint(n),np.random.randint(n)]=2*np.random.randint(1,3)
        self.matrix[np.random.randint(n),np.random.randint(n)]=2*np.random.randint(1,3)
    
    def display_grid(self):
        '''
        Method to display the grid
        parameters:none
        return : none
        '''
        for i in range(self.GRID_SIZE):
            
            print('+------'*self.GRID_SIZE,end='+\n')
            print('| ',end='')
            
            for j in range(self.GRID_SIZE):
                print(f'{self.matrix[i,j]:>4}',end=' | ')
            
            print()
        
        print('+------'*self.GRID_SIZE,end='+\n')

    def left(self):
        '''
        Merge tiles left
        parameters: none
        return : none
        '''
        for i in range(self.GRID_SIZE):
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
        '''
        Merge tiles right
        parameters: none
        return : none
        '''
        for i in range(self.GRID_SIZE):
            non_zero_terms=self.matrix[i][self.matrix[i]>0]
            self.matrix[i,:]=0
            idx=len(non_zero_terms)-1
            j=self.GRID_SIZE-1
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
        '''
        Merge tiles up
        parameters:none
        return : none
        '''
        for i in range(self.GRID_SIZE):
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
        '''
        Merge tiles down
        parameters: none
        return : none
        '''
        for i in range(self.GRID_SIZE):
            non_zero_terms=self.matrix[:,i][self.matrix[:,i]>0]
            self.matrix[:,i]=0
            idx=len(non_zero_terms)-1
            j=self.GRID_SIZE-1
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
        '''
        Finds all the empty locations in the grid and returns an array of tuples where each tuple gives the empty location indices (row,column)
        parameters: none
        return: array of tuples
        '''
        empty_locations=[]
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if self.matrix[i,j]==0:
                    empty_locations.append((i,j))
        return empty_locations

    def fill_empty_location(self):
        '''
        Randomly fills an empty location if exists.
        If empty location does not exist, no changes are made.
        parameters: none
        returns none
        '''
        empty_locations=self.find_empty_locations()
        if len(empty_locations)==0:
            return
        loc_to_fill=empty_locations[np.random.randint(len(empty_locations))]
        self.matrix[loc_to_fill[0],loc_to_fill[1]]=2*np.random.randint(1,3)

    def max_elem(self):
        '''
        Finds and returns the numerically greatest element in the matrix.
        parameters: none
        return: int (maximum value) 
        '''
        return np.max(self.matrix)