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

	def get_medians1(self, A, B):
		def find_kth(A, B, k):
			lenA, lenB = len(A), len(B)
			if lenA > lenB:
				return find_kth(B, A, k)
			left, right = 0, lenA
			while left < right:
				mid = left + (right - left) / 2
				if 0 <= k - 1 - mid < lenB and A[mid] >= B[k - 1 - mid]:
					right = mid
				else:
					left = mid + 1
			Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
			Bj = B[k - left - 1] if k - 1 - left >= 0 else float("-inf")
			return max(Ai_minus_1, Bj)

		m, n = len(A), len(B)
		return (find_kth(A, B, (m + n + 1) / 2) + find_kth(A, B, (m + n + 2) / 2)) / 2.0

	def get_medians2(self, A, B):
		"""
		1) len(left_part) == len(right_part)
    2) max(left_part) <= min(right_part)
		"""
		m, n = len(A), len(B)
		if m > n:
			A, B, m, n = B, A, n, m
		if n == 0:
			raise ValueError
		imin, imax, half_len = 0, m, (m + n + 1) / 2
		while imin <= imax:
			i = (imin + imax) / 2
			j = half_len - i
			if i < m and A[i] < B[j - 1]:
				imin = i + 1
			elif i > 0 and A[i - 1] > B[j]:
				imax = i - 1
			else:
				if i == 0:
					max_of_left = B[j - 1]
				elif j == 0:
					max_of_left = A[i - 1]
				else:
					max_of_left = max(A[i - 1], B[j - 1])
				if (m + n) % 2 == 1:
					return max_of_left

				if i == m:
					min_of_right = B[j]
				elif j == n:
					min_of_right = A[i]
				else:
					min_of_right = min(A[i], B[j])
				return (max_of_left + min_of_right) / 2.0

s=Solution()
print s.get_medians([1], [1])
print s.get_medians([1,2], [3])
print s.get_medians1([1], [1])
print s.get_medians1([1, 2], [3])
print s.get_medians2([1], [1])
print s.get_medians2([1, 2], [3])
