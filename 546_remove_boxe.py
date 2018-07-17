"""
546 remove boxes
"""


class Solution(object):
	def remove_boxes(self, boxes):
		"""
		dp(i, j, k) which denotes the maximum points possible by removing the boxes of subarray boxes[i, j] with k boxes
		attached to its left of the same color as boxes[i]
		"""
		n = len(boxes)
		dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
		for i in range(n):
			for k in range(i + 1):
				dp[i][i][k] = (k + 1) * (k + 1)
		for l in range(1, n):
			for j in range(l, n):
				i = j - l
				for k in range(0, i + 1):
					res = (k + 1) * (k + 1) + dp[i + 1][j][0]
					for m in range(i + 1, j + 1):
						if boxes[m] == boxes[i]:
							res = max(res, dp[i + 1][m - 1][0] + dp[m][j][k + 1])
					dp[i][j][k] = res
		return 0 if n == 0 else dp[0][n - 1][0]


print Solution().remove_boxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
