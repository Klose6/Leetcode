"""
64 minimum path sum
"""


def min_path_sum(grid):
	m, n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			if not i and j:
				grid[i][j] += grid[i][j - 1]
			elif i and not j:
				grid[i][j] += grid[i - 1][j]
			elif i and j:
				grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
	return grid[i - 1][j - 1]
