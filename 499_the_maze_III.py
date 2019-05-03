"""
The maze III 499

https://discuss.leetcode.com/category/648/the-maze-iii
http://www.cnblogs.com/grandyang/p/6746528.html
https://discuss.leetcode.com/topic/77076/simple-python-explanation
"""
from heapq import heappush, heappop

def findPath(start, hole, board):
  if not start or not hole or not board:
    return []
  # using dijkstra to find the shortest path (store the path to the result)
  m, n = len(board), len(board[0])
  def go(c, i, j):
    x,y = c
    d = 0
    while 0 <= x+i < m and 0 <= y+j < n and board[x+i][y+j] == "0":
      if (x, y) == hole:
        break
      x, y = x+i, y+j
      d += 1
    return d,(x,y)
  q = list()
  visited = set()
  heappush(q, (0, "", start))
  # using the (distance, path, points) in the heap,
  # which guarantees to find the lexicographically smaller path first
  while q:
    count, path, cur = heappop(q)
    # print(count, path, cur)
    if cur in visited:
      continue
    visited.add(cur)
    if cur == hole:
      return path
    for d, i, j in [("u", -1, 0), ("l", 0, -1), ("r", 0, 1), ("d", 1, 0)]:
      l, point = go(cur, i, j)
      heappush(q, (l+count, path+d, point))
  return "impossible"

board = [list("00000"),
list("11001"),
list("00000"),
list("01001"),
list("01000")]
start, end = (4,3), (0,1)
print(findPath(start, end, board)) #"lul"