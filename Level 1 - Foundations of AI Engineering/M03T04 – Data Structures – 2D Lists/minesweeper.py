#Create a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot
def create_minesweeper_grid():
    # Define the grid as a list of lists
    grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]
    return grid

#Return a grid where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot, i.e., horizontally, vertically, and diagonally
def calculate_mine_counts(grid):
    # Create a new grid to store mine counts
    mine_counts = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    # Directions for adjacent cells (8 directions)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                # If it's a mine, increment the count for all adjacent cells
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == "-":
                        mine_counts[ni][nj] += 1
    
    return mine_counts

#Print the grid with mine counts
def print_mine_counts(mine_counts):
    for row in mine_counts:
        print(" ".join(str(cell) for cell in row))

# Create the minesweeper grid
grid = create_minesweeper_grid()
    
# Calculate mine counts
mine_counts = calculate_mine_counts(grid)
    
    # Print the mine counts grid
print("Minesweeper Grid with Mine Counts:")
print_mine_counts(mine_counts)
