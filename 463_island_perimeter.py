"""
463 island perimeter
"""

def islandPerimeter(grid):
  """
  find all the cell 1s -m  and the total number of neighbors -n , then 4*m-2*n
  """
  if not grid: return 0
  cells, neighbors = 0, 0
  m, n = len(grid), len(grid[0])
  for i in range(m):
    for j in range(n):
      if grid[i][j] == 1:
        cells += 1
        if j < n-1 and grid[i][j+1] == 1:
          neighbors += 1
        if i < m-1 and grid[i+1][j] == 1:
          neighbors += 1
  return 4 * cells - 2 * neighbors

print(islandPerimeter([
  [0,1,0,0,],
  [1,1,1,0],
  [0,1,0,0],
  [1,1,0,0]
])) # 16