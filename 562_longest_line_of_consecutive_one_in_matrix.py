"""
562 longest line of consecutive one in matrix
"""


def find_the_longest_one(matrix):
  if not matrix:
    return 0
  res = 0
  m, n = len(matrix), len(matrix[0])
  diagonal = [[0] * n for _ in range(m)]
  # process the horizontal and diagonal
  for i in range(m):
    count = 0
    for j in range(n):
      count = matrix[i][j] * (count + 1)
      diagonal[i][j] = matrix[i][j]  # for the first row
      if i > 0 and j > 0:
        diagonal[i][j] = diagonal[i][j] * (diagonal[i - 1][j - 1] + 1)
      res = max(diagonal[i][j], count, res)
  # process the vertical and anti-diagonal
  diagonal = [[0] * n for _ in range(m)]
  for j in range(n):
    count = 0
    for i in range(m):
      count = matrix[i][j] * (count + 1)
      diagonal[i][j] = matrix[i][j]  # for the first column
      if j > 0 and i < m - 1:
        diagonal[i][j] = diagonal[i][j] * (diagonal[i + 1][j - 1] + 1)
      res = max(res, count, diagonal[i][j])
  return res


print(find_the_longest_one([
  [0, 1, 1],
  [0, 1, 0],
  [1, 0, 1]
]))  # 3
