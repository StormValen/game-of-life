# Python v.3.8.2
import time
import random

# PyGame v.1.9.6
import pygame   

# NumPy v.1.18.4
import numpy as np

BACKGROUND_COLOR = (25, 25, 25)
SCREEN_SIZE = (900,600)
CELL_SIZE = 10

pygame.init()

# Create new window.
screen = pygame.display.set_mode(size=SCREEN_SIZE)

num_columns = int(SCREEN_SIZE[0] / CELL_SIZE)
num_rows = int(SCREEN_SIZE[1] / CELL_SIZE)
print('GRID R: {}, C: {}' .format(num_rows, num_columns))

# Create grid numpy
grid = np.zeros((num_columns, num_rows))

grid[12, 25] = 1
grid[12, 26] = 1
grid[12, 27] = 1

# Grid loop
iteration_counter = 0
while True:
    
    print('Iteration {}'.format(iteration_counter))
    
    new_grid = grid
    
    screen.fill(BACKGROUND_COLOR)

    for y in range(num_rows):
        for x in range(num_columns):

            # Drawing current Grid.

            cell_position = (x * CELL_SIZE, y * CELL_SIZE)
            my_rect = pygame.Rect(cell_position, (CELL_SIZE, CELL_SIZE))

            cell_status = int(grid[x,y])

            # cell_status = 0 (cell dead) will fill the rectangle.
            if cell_status == 0:
                pygame.draw.rect(screen, (125, 125, 125), my_rect, 1)
            
            # cell_status = 1 (cell alive) will draw the borders.
            elif cell_status == 1:
                pygame.draw.rect(screen, (255, 255, 255), my_rect, 0)



            # Calculate new Grid.

            neigh_sum = grid[(x-1) % num_columns, (y-1) % num_rows] + grid[(x) % num_columns, (y-1) % num_rows] + grid[(x+1) % num_columns, (y-1)  % num_rows] + \
                        grid[(x-1) % num_columns, (y)   % num_rows]                                               + grid[(x+1) % num_columns, (y+1)  % num_rows] + \
                        grid[(x-1) % num_columns, (y+1) % num_rows] + grid[(x) % num_columns, (y+1) % num_rows] + grid[(x+1) % num_columns, (y+1)  % num_rows]

            # Any live cell with 2 or 3 neighbours alive survives.
            if neigh_sum <= 2 or neigh_sum >= 3 and grid[x,y] == 0:
                new_grid[x,y] == 0

            # Any dead cell with 3 alive neighbours becomes a live cell.
            elif neigh_sum == 3 and grid[x,y] == 0:
                new_grid[x,y] = 1
            else:
                new_grid[x,y] == 0
            

    

    # Updates screen with new content.
    pygame.display.flip()

    # Assign new grid to current grid.
    grid = new_grid
    
    iteration_counter += 1

pygame.quit()    