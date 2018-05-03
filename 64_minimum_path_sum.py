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


def min_path_sum2(grid):
	m, n = len(grid), len(grid[0])
	dp = [0] * n
	dp[0] = grid[0][0]
	for j in range(1, n):
		dp[j] = dp[j - 1] + grid[0][j]
	for i in range(1, m):
		dp[0] += grid[i][0]
		for j in range(1, n):
			dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
	return dp[n - 1]
