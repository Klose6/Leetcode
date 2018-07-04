"""
862 shortest subarray with sum at least k
"""
import collections


class Solution(object):
	def shortestSubarray(self, A, K):
		N = len(A)
		B = [0] * (N + 1)
		for i in range(N): B[i + 1] = B[i] + A[i]
		# Deque d will keep indexes of increasing B[i].
		d = collections.deque()
		res = N + 1
		for i in xrange(N + 1):
			while d and B[i] - B[d[0]] >= K:
				res = min(res, i - d.popleft())
			while d and B[i] <= B[d[-1]]:
				d.pop()
			d.append(i)
		return res if res <= N else -1


print Solution().shortestSubarray([2, -1, 2], 3)
