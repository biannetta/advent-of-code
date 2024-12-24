puzzleInput="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

directions = [
  (0,-1),   # Left
  (0,1),    # Right
  (-1,0),   # Up
  (1,0),    # Down
  (-1,-1),  # Up-Left
  (1,-1),   # Down-Left
  (-1,1),   # Up-Right
  (1,1)     # Down-Right
]
grid = [list(line.strip()) for line in puzzleInput.splitlines()]
rows = len(grid)
cols = len(grid[0])
word = "XMAS"
count = 0

def is_valid(curX, curY, dX, dY):
  return 0 <= curX + 3*dX < rows and 0 <= curY + 3*dY < cols

def match_word(curX, curY, dX, dY):
  for i in range(len(word)):
    if grid[curX + i*dX][curY + i*dY] != word[i]:
      return False
  return True

for i in range(rows):
  for j in range(cols):
    for dx, dy in directions:
      if is_valid(i,j,dx,dy) and match_word(i,j,dx,dy):
        count +=1

print(count)