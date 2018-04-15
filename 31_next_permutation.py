"""
31 next permutation
"""

class Solution(object):
	def reverse(self, nums, l,r):
		while l<r:
			nums[l], nums[r] = nums[r], nums[l]
			l+=1
			r-=1
	def get_next_permutation(self, nums):
		if not nums:
			return
		n=len(nums)
		i = n-1
		while i>0:
			if nums[i] > nums[i-1]:
				break
			i-=1
		if i == 0:
			return nums[::-1]
		else:
			self.reverse(nums, i, n-1)
			idx=i
			while idx<n:
				if nums[idx]>nums[i-1]:
					break
				idx+=1
			nums[i-1], nums[idx] = nums[idx],nums[i-1]
			return nums
s=Solution()
print s.get_next_permutation([1,2,3])
print s.get_next_permutation([3,2,1])
print s.get_next_permutation([1,1,3])