"""
208 wiggle sort
"""

class Solution:
	def wiggle_sort(self, nums):
		if not nums:
			return
		for i in range(len(nums)):
			nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)
		return nums
s= Solution()
print s.wiggle_sort([3,5,2,1,6,4])