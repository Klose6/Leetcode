"""
4 median of two sorted arrays
"""

import sys

class Solution(object):
	def get_medians(self, A, B):
		l, r = (len(A)+len(B)+1)>>1, (len(A)+len(B)+2)>>1
		return (self.get_kth(A, 0, B, 0, l) +
						self.get_kth(A, 0, B, 0, r)) / 2.0
	def get_kth(self, A, astart, B, bstart, k):
		if astart >= len(A):
			return B[bstart+k-1]
		if bstart >= len(B):
			return A[astart+k-1]
		if k==1:
			return min(A[astart], B[bstart])

		amid, bmid = sys.maxint, sys.maxint
		if astart+k/2-1 < len(A):
			amid = A[astart+k/2-1]
		if bstart+k/2-1 < len(B):
			bmid = B[bstart+k/2-1]
		if amid<bmid:
			return self.get_kth(A, astart+k/2, B, bstart, k-k/2)
		else:
			return self.get_kth(A, astart, B, bstart+k/2, k-k/2)

s=Solution()
print s.get_medians([1], [1])
print s.get_medians([1,2], [3])