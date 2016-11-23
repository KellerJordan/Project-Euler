grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
    
vert = max([(grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]) for i in range(17) for j in range(20)])
hori = max([(grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]) for i in range(20) for j in range(17)])
ldia = max([(grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]) for i in range(17) for j in range(17)])
rdia = max([(grid[i][j + 3] * grid[i + 1][j + 2] * grid[i + 2][j + 1] * grid[i + 3][j]) for i in range(17) for j in range(17)])

m = max(vert, hori, ldia, rdia)
print(m)
