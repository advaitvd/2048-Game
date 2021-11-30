from Grid import Grid        

def game_over(grid):
    for i in range(Grid.GRID_SIZE-1):
        for j in range(Grid.GRID_SIZE-1):
            if grid.matrix[i,j]==grid.matrix[i,j+1] or grid.matrix[i,j]==grid.matrix[i+1,j] or grid.matrix[i,j]==0:
                return False
    
    for i in range (Grid.GRID_SIZE-1):
        if grid.matrix[i,Grid.GRID_SIZE-1]==grid.matrix[i+1,Grid.GRID_SIZE-1] or grid.matrix[Grid.GRID_SIZE-1,i]==grid.matrix[Grid.GRID_SIZE-1,i+1] or grid.matrix[Grid.GRID_SIZE-1,i]==0 or grid.matrix[i,Grid.GRID_SIZE-1]==0:
            return False
    if grid.matrix[Grid.GRID_SIZE-1,Grid.GRID_SIZE-1]==0:
        return False
    return True

def run():
    grid=Grid(Grid.GRID_SIZE)
    print('Welcome to the game! This is what you start with.')
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
            if grid.max_elem()==Grid.WIN_SCORE:
                print('Congratulations! You acheived the winning score.')
            else:
                print('Game Over! Try again...')
            break

if __name__ == "__main__":
    run()