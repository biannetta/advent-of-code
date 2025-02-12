def read_input(file_path):
    with open(file_path, 'r') as file:
        # Read the file and create a 2D grid (list of lists)
        return [list(line.strip()) for line in file.readlines()]

def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    count = 0

    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1), # Left
        (-1, 0), # Up
        (1, 1),  # Down-right diagonal
        (1, -1), # Down-left diagonal
        (-1, 1), # Up-right diagonal
        (-1, -1) # Up-left diagonal
    ]

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if is_valid(i, j, dx, dy, rows, cols) and match_word(grid, i, j, dx, dy, word):
                    count += 1
    return count

def is_valid(x, y, dx, dy, rows, cols):
    # Check if the (x, y) start point and direction (dx, dy) stay within bounds
    return 0 <= x + 3*dx < rows and 0 <= y + 3*dy < cols

def match_word(grid, x, y, dx, dy, word):
    # Check if the word can be matched starting from (x, y) in the given direction
    for i in range(len(word)):
        if grid[x + i*dx][y + i*dy] != word[i]:
            return False
    return True

# Main Execution
file_path = r"P:\ScriptHub\Scripts\Python\AdventOfCode\Day4Input.txt"
grid = read_input(file_path)
print(find_xmas(grid))  # Output will be the total count of "XMAS" in the grid
