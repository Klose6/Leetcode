"""
The maze II 505
https://leetcode.com/articles/the-maze-ii/
https://discuss.leetcode.com/topic/77472/similar-to-the-maze-easy-understanding-java-bfs-solution
https://discuss.leetcode.com/topic/77975/python-solution-with-explanation-dijkstra-s-algorithm/2
"""
from sys import maxsize
from queue import Queue
from heapq import heappush, heappop

def getPath(start, end, maze):
  """
  BFS solution
  """
  if not maze:
    return -1
  m, n = len(maze), len(maze[0])
  q = Queue()
  q.put(start)
  distance = [[maxsize for _ in range(n)] for _ in range(m)]
  # distance = [maxsize * n] * m # don't usie this, the 4th columns will be all 0
  distance[start[0]][start[1]] = 0
  # distance[0][4] = 0
  # print(distance)
  while not q.empty():
    cur = q.get()
    # print(cur[0], cur[1])
    for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
      x = cur[0]
      y = cur[1]
      count = 0
      while 0<=x+dir[0]<m and 0<=y+dir[1]<n and maze[x+dir[0]][y+dir[1]] == "0":
        x += dir[0]
        y += dir[1]
        count += 1
      if distance[cur[0]][cur[1]] + count < distance[x][y]:
        # only add the elements with shorter distances(non-visited elements)
        distance[x][y] = distance[cur[0]][cur[1]] + count
        q.put((x, y))
        # print("put({}, {})".format(x, y))
  return distance[end[0]][end[1]] if distance[end[0]][end[1]] != maxsize else -1

def getPath_1(start, end, maze):
  """
  Dijkstra algorithm
  """
  if not maze:
    return -1
  visited = set()
  m, n = len(maze), len(maze[0])
  q = []
  heappush(q, (0, start))
  def go(point, d):
    i, j = point
    l = 0
    while 0<=i+d[0]<m and 0<=j+d[1]<n and maze[i+d[0]][j+d[1]] != "1":
      i += d[0]
      j += d[1]
      l += 1
    return l, (i, j)
  while q:
    length, cur = heappop(q)
    if cur in visited:
      continue
    visited.add(cur)
    if cur == end:
      return length
    for dir in {(-1, 0), (1, 0), (0, 1), (0,-1)}:
      l, point = go(cur, dir)
      heappush(q, (l+length, point))
  return -1

maze = ["00100", "00000", "00010", "11011", "00000"]
print(getPath((0,4), (4,4), maze)) #12
print(getPath_1((0,4), (4,4), maze)) #12

# a = set()
# a.add((1,2))
# a.add((1,2))
# print(a)