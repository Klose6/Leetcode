"""
861 score after flipping matrix
Assume A is M * N.

A[i][0] is worth 1 << (N - 1) points, more than the sum of (A[i][1] + .. + A[i][N-1]).
We need to toggle all A[i][0] to 1, here I toggle all lines for A[i][0] = 0.
A[i][j] is worth 1 << (N - 1 - j)
For every col, I count the current number of 1s.
After step 1, A[i][j] becomes 1 if A[i][j] == A[i][0].
if M - cur > cur, we can toggle this column to get more 1s.
max(M, M - cur) will be the maximum number of 1s that we can get.
"""


class Solution(object):
	def scores(self, A):
		M, N = len(A), len(A[0])
		res = (1 << N - 1) * M
		for j in range(1, N):
			cur = sum(A[i][j] == A[i][0] for i in range(M))
			res += max(cur, M - cur) * (1 << N - 1 - j)
		return res


print Solution().scores([
	[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]
])  # 39
