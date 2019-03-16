"""
576 out of boundary paths
"""


def findOutOfBoundaryPaths(m, n, N, x, y):
  M = [[0 for _ in range(n)] for _ in range(m)]
  for _ in range(N):
    M = [
      [(i == 0 or M[i - 1][j]) + (i == m - 1 or M[i + 1][j])
       + (j == 0 or M[i][j - 1]) + (j == n - 1 or M[i][j + 1])
       for i in range(n)] for j in range(m)
    ]
  return M[x][y] % (10 ** 9 + 7)


print(findOutOfBoundaryPaths(2, 2, 2, 0, 0))
