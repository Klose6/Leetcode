"""
62 unique paths
"""


def unique_paths(m, n):
	dp = [[1] * n for _ in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = 0
			if i - 1 >= 0:
				dp[i][j] += dp[i - 1][j]
			if j - 1 >= 0:
				dp[i][j] += dp[i][j - 1]
	return dp[m - 1][n - 1]


def unique_paths2(m, n):
	cur = [1] * n
	for i in range(1, m):
		for j in range(1, n):
			cur[j] += cur[j - 1]
	return cur[n - 1]


print unique_paths(3, 2)  # 3
print unique_paths(7, 3)  # 28
print unique_paths2(3, 2)  # 3
print unique_paths2(7, 3)  # 28
