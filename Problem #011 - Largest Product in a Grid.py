"""
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in a 20x20 grid?
"""

grid = []

for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    
    for _ in range(3):
        grid_t.insert(0, 0)
        grid_t.append(0)
    
    grid.append(grid_t)

for _ in range(3):
    grid.insert(0, [0] * 26)
    grid.append([0] * 26)

toReturn = 0

for i in range(3, 23):
    for j in range(3, 23):
        rightProd = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
        rDiagProd = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
        bottomProd = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
        lDiagProd = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
        
        toReturn = max(toReturn, rightProd, rDiagProd, bottomProd, lDiagProd)

print(toReturn)
