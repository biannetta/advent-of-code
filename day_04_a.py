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
  (0,-1),
  (0,1),
  (-1,0),
  (1,0),
  (-1,-1),
  (1,-1),
  (-1,1),
  (1,1)
]
rows = []

for line in puzzleInput.splitlines():
  rows.append(list(line))

print(rows)