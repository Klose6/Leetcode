"""
668 kth smallest number in multiplication table
"""

class Solution(object):
	def find_kth_number(self, m, n, k):
		def enough(x):
			return sum((min(x/i, n) for i in xrange(1, m+1))) >= k
		lo, hi = 1, m*n
		while lo<hi:
			mid = (lo+hi)/2
			if not enough(mid):
				lo=mid+1
			else:
				hi=mid
		return lo
s=Solution()
print s.find_kth_number(3,3,5) #3
print s.find_kth_number(2,3,6) #6