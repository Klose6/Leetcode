"""
45 jump game II
"""


def jump(nums):
	# BFS, O(n)
	if not nums or len(nums) < 2:
		return 0
	n = len(nums)
	steps = 0
	i = 0
	cur_max, next_max = 0, 0
	while cur_max - i + 1 > 0:
		steps += 1
		while i <= cur_max:
			next_max = max(next_max, nums[i] + i)
			if next_max >= n - 1:
				return steps
			i += 1
		cur_max = next_max
	return 0


def jump2(nums):
	if not nums:
		return 0
	n = len(nums)
	steps = 0
	cur_end = 0
	next_max = 0
	for i in range(n - 1):
		next_max = max(next_max, nums[i] + i)
		if i == cur_end:
			steps += 1
			cur_end = next_max
	return steps if next_max >= n - 1 else 0


print jump([2, 3, 1, 1, 4])  # 2
print jump2([2, 3, 1, 1, 4])  # 2
