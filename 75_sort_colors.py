"""
75 Sort colors
"""


def sort_colors(nums):
	if not nums:
		return nums
	n = len(nums)
	lo, hi = 0, n - 1
	i = 0
	while i < hi:
		if i != lo and nums[i] == 0:
			nums[lo], nums[i] = nums[i], nums[lo]
			lo += 1
		if i != hi and nums[i] == 2:
			nums[hi], nums[i] = nums[i], nums[hi]
			hi -= 1
		i += 1
	return nums


print sort_colors([2, 0, 2, 1, 1, 0])
