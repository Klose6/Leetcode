import re

#https://discuss.leetcode.com/topic/77493/python-bfs-solution
#http://www.cnblogs.com/grandyang/p/6381458.html
def can_stop(matrix, start, dest):
  #using bfs
  q = (start)
  dirs = ((1, 0), (-1, 0), (0,1), (0, -1))
  visited = [start]
  while q:
    i, j = q.pop(0)
    if i == dest[0] and j == dest[1]:
      return True
    for x, y in dirs:
      col = i + x;
      row = j + y;
      while 0<=col<n and 0<=row<n and matrix[col][row] != 1:
        col += x
        row += y
      col -= x
      row -= y
      if (col, row) not in visited and matrix[row][col] == 0:
        q.append((col, row))
        visited.append((col, row))
  return False

l = [(1,0)]
print((1,0) in l)