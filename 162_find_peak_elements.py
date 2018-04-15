"""
162 find peak elements
"""

class Solution(object):
	def find_peak_elements(self, nums):
		if not nums:
			return
		lo, hi = 0, len(nums)-1
		while lo < hi:
			mid = lo+(hi-lo)/2
			mid2 = mid+1
			if nums[mid] < nums[mid2]:
				lo=mid2
			else:
				hi=mid
		return nums[lo]
s=Solution()
print s.find_peak_elements([1])
print s.find_peak_elements([1,2])
print s.find_peak_elements([2,1])
print s.find_peak_elements([1,3,2])