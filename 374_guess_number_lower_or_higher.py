"""
374 Guess number lower or higher
"""

class Solution(object):
	def guess_number(self, n):
		low, high = 1,n
		while low < high:
			mid = low+(high-low)/2
			low, high = ((mid, mid), (mid+1, high), (low, mid-1))[guess(mid)]
		return low