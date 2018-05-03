"""
63 unique paths II
"""


def unique_paths_with_obstacles(grid):
	if not grid:
		raise ValueError("Invalid input")
	m, n = len(grid), len(grid[0])
	dp = [0] * n
	dp[0] = 1
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				dp[j] = 0
			else:
				dp[j] += dp[j - 1]
	return dp[n - 1]
