"""
72 edit distance
"""


def min_distance(w1, w2):
	m, n = len(w1), len(w2)
	dp = [[0] * (n + 1) for _ in range(m + 1)]
	for i in range(1, m + 1):
		dp[i][0] = i
	for i in range(1, n + 1):
		dp[0][i] = i
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if w1[i] == w2[j]:
				dp[i][j] = dp[i - 1][j - 1]
			else:
				dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
	return dp[m][n]