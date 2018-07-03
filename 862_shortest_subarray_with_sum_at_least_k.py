"""
862 shortest subarray with sum at least k
"""
import collections


class Solution(object):
	def shortestSubarray(self, A, K):
		N = len(A)
		B = [0] * (N + 1)
		for i in range(N): B[i + 1] = B[i] + A[i]
		d = collections.deque()
		res = N + 1
		for i in range(N + 1):
			while d and B[i] - B[d[0]] >= K:
				res = min(res, i - d.popleft())
			while d and B[i] <= B[d[-1]]:
				d.pop()
		return res if res <= N else -1
