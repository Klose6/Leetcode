"""
490 the maze
"""
from queue import Queue

def hasPath(matrix, start, dest):
  if not matrix: raise ValueError("Wrong input")
  m, n = len(matrix), len(matrix[0])
  q = Queue()
  q.put(start)
  visited = {tuple(start)} # list is not hashable
  while not q.empty():
    cur = q.get()
    # print(f"cur: {cur}")
    if cur == tuple(dest): return True
    for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      x = cur[0] #+ d[0]
      y = cur[1] #+ d[1]
      while 0<=x+d[0]<m and 0<=y+d[1]<n and matrix[x+d[0]][y+d[1]] == "0": # keep going until meet a wall
        x += d[0]
        y += d[1]
      # x -= d[0] # roll back the valid position
      # y -= d[1]
      if (x, y) not in visited:
        visited.add((x, y))
        q.put((x, y))
  return False

matrix = [list("00100"), list("00000"), list("00010"), list("11011"), list("00000")]
print(hasPath(matrix, [0,4], [4,4])) # True
print(hasPath(matrix, [0,4], [3,2])) # False