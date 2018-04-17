"""
1 Two sum
"""


class Solution(object):
	def two_sum(self, nums, target):
		# O(n)
		if not nums or len(nums) <= 1:
			return
		buff_dict = {}
		for i in range(len(nums)):
			if nums[i] in buff_dict:
				return [buff_dict[nums[i]], i]
			else:
				buff_dict[target - nums[i]] = i


s = Solution()
print s.two_sum([2, 7, 11, 15], 9)  # [0,1]
