"""
Pacific Atlantic water flow 417
"""
result = []

def pacific_atlantic(matrix):
  if not matrix:
    return matrix
  m, n = len(matrix), len(matrix[0])
  result = [[0 for _ in range(m)] for _ in range(n)]
  for i in range(m):
    bfs(matrix, i, 0)
  for i in range(1, n):
    bfs(matrix, 0, i)
  for i in range(n):
    bfs(matrix, m-1, i)
  for i in range(m-1):
    bfs(matrix, i, n-1)
  return result

def bfs(matrix, i, j):
  pass