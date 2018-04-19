"""
18 4sum
"""


def four_sum(nums, target):
	def find_N_sum(nums, target, N, cur_res, results):
		if not nums or len(nums) < N or N < 2 or target < N * nums[0] or target > N * nums[-1]:
			return
		if N == 2:
			l, r = 0, len(nums) - 1
			while l < r:
				s = nums[l] + nums[r]
				if s == target:
					results.append(cur_res + [nums[l], nums[r]])
					while l < r and nums[l] == nums[l + 1]: l += 1
					while l < r and nums[r] == nums[r - 1]: r -= 1
					l += 1
					r -= 1
				elif s < target:
					l += 1
				else:
					r -= 1
		else:
			for i in range(len(nums) - N + 1):
				if i == 0 or i > 0 and nums[i] != nums[i - 1]:
					find_N_sum(nums[i + 1:], target - nums[i], N - 1, cur_res + [nums[i]], results)

	results = []
	find_N_sum(sorted(nums), target, 4, [], results)
	return results


print four_sum([1, 0, -1, 0, -2, 2], 0)
