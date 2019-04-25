"""
01 matrix 542
https://discuss.leetcode.com/topic/83453/java-solution-bfs
https://discuss.leetcode.com/topic/83558/java-33ms-solution-with-two-sweeps-in-o-n
"""
from sys import maxsize
from queue import Queue


def findDistanceToOne(matrix):
  if not matrix:
    return None
  m, n = len(matrix), len(matrix[0])
  q = Queue()
  for i in range(m):
    for j in range(n):
      if matrix[i][j] == 1:
        matrix[i][j] = maxsize # mark all the 1s since later we need to set the distances, which can be als o1
      else:
        q.put((i, j)) # store the positions of 0s in the queue for bfs
  while not q.empty():
    x, y = q.get()
    for dir in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
      a, b = x + dir[0], y + dir[1]
      if 0 <= a <m and 0 <= b <n and matrix[a][b] == maxsize:
        q.put((a,b)) # store the positions of 1s for bfs
        matrix[a][b] = min(matrix[a][b], matrix[x][y]+1)
  return matrix

def findDistanceToOne_2(matrix):
  if not matrix:
    return None
  m,n = len(matrix), len(matrix[0])
  for i in range(m):
    for j in range(n):
      if matrix[i][j] == 0:
        continue
      up = matrix[i][j-1] if j > 0 else maxsize
      left = matrix[i-1][j] if i > 0 else maxsize
      matrix[i][j] = min(up, left) + 1
  for i in range(m)[::-1]:
    for j in range(n)[::-1]:
      if matrix[i][j] == 0:
        continue
      right = matrix[i][j+1] if j < n-1 else maxsize
      down = matrix[i+1][j] if i < m-1 else maxsize
      matrix[i][j] = min(matrix[i][j], min(down, right)+1)
  return matrix

print(findDistanceToOne([[0,0,0], [0,1,0], [0,0,0]]))
print(findDistanceToOne([[0,0,0], [0,1,0], [1,1,1], [1,1,1]]))

print(findDistanceToOne_2([[0,0,0], [0,1,0], [0,0,0]]))
print(findDistanceToOne_2([[0,0,0], [0,1,0], [1,1,1], [1,1,1]]))


def findDisOne(matrix):
  if not matrix:
    return None
  m, n = len(matrix), len(matrix[0])
  dis = [[maxsize for _ in range(m)] for _ in range(n)]
  for i in range(m):
    for j in range(n):
      if matrix[i][j] == 0:
        dis[i][j] = 0
        continue
      if i-1 >=0 and matrix[i-1][j] == 0 or i+1 < m and matrix[i+1][j] == 0 or \
        j-1 >=0 and matrix[i][j-1] == 0 or j+1 < n and matrix[i][j+1] == 0:
        dis[i][j] = 1
      elif i-1 >= 0 and dis[i-1][j] != maxsize or i+1 < m and dis[i+1][j] != maxsize or \
        j-1 >=0 and dis[i][j-1] != maxsize or j+1 < n and dis[i][j+1] != maxsize:
        cur_dis = maxsize
        if i-1 >= 0 and dis[i-1][j] != maxsize:
          cur_dis = min(cur_dis, dis[i-1][j])
        if i+1 < m and dis[i+1][j] != maxsize:
          cur_dis = min(cur_dis, dis[i+1][j])
        if j-1 >= 0 and dis[i][j-1] != maxsize:
          cur_dis = min(cur_dis, dis[i][j-1])
        if j+1 < n and dis[i][j+1] != maxsize:
          cur_dis = min(cur_dis, dis[i][j+1])
        dis[i][j] = cur_dis + 1
      else:
        dis[i][j] = bfs(matrix, i, j)
  return dis

def bfs(matrix, i, j):
  m, n = len(matrix), len(matrix[0])
  q = Queue()
  q.put((0, (i, j)))
  while q:
    d, point = q.get()
    if matrix[point[0]][point[1]] == 0:
      return d
    for dir in [(-1,0), (1,0), (0,-1), (0,1)]:
      if 0<=point[0]+dir[0]<m and 0<=point[1]+dir[1]<n:
        q.put((d+1, (point[0]+dir[0], point[1]+dir[1])))
  return maxsize
