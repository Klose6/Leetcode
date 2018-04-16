"""
801 Minimum swaps to make sequences increasing
"""

class Solution(object):
	def min_swaps(self, A, B):
		n = len(A)
		swap, no_swap = [n]*n, [n]*n
		swap[0], no_swap[0]= 1, 0
		for k in range(1, n):
			if A[k] > A[k-1] and B[k] > B[k-1]:
				no_swap[k] = no_swap[k-1]
				swap[k] = swap[k-1] + 1
			if A[k-1] < B[k] and B[k-1] < A[k]:
				no_swap[k] = min(no_swap[k], swap[k-1])
				swap[k] = min(swap[k], no_swap[k-1]+1)
		return min(swap[-1], no_swap[-1])

s=Solution()
print s.min_swaps([1,3,5,4], [1,2,3,7]) #1
