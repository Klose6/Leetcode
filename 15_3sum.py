"""
15 3sum
"""


class Solution(object):
	def three_sum(self, nums):
		if not nums:
			return
		nums = sorted(nums)
		res = []
		for i in range(len(nums) - 2):
			if i > 0 and nums[i] == nums[i - 1]: continue
			l, r = i + 1, len(nums) - 1
			while l < r:
				cur_sum = nums[i] + nums[l] + nums[r]
				if cur_sum == 0:
					res.append([nums[i], nums[l], nums[r]])
					while l < r and nums[l] == nums[l + 1]: l += 1
					while l < r and nums[r] == nums[r - 1]: r -= 1
					l += 1
					r -= 1
				elif cur_sum > 0:
					r -= 1
				else:
					l += 1
		return res


s = Solution()
print s.three_sum([-1, 0, 1, 2, -1, -4])
