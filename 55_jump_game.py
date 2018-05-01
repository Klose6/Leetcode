"""
55 jump game
"""


def can_jump(nums):
	if not nums:
		raise ValueError("invalid input")
	idx = 0
	for i in range(len(nums)):
		if i <= idx:
			idx = max(idx, nums[i] + i)
	return idx >= len(nums) - 1


def can_jump2(nums):
	if not nums:
		raise ValueError("invalid input")
	i, reach = 0, 0
	n = len(nums)
	while i < n and i <= reach:
		reach = max(reach, i + nums[i])
		i += 1
	return i == n


def can_jump3(nums):
	if not nums:
		raise ValueError("invalid input")
	goal = len(nums) - 1
	for i in range(len(nums))[::-1]:
		if nums[i] + i >= goal:
			goal = i
	return not goal

print can_jump([2, 3, 1, 1, 4])  # true
print can_jump([3, 2, 1, 0, 4])  # false
print can_jump2([2, 3, 1, 1, 4])  # true
print can_jump2([3, 2, 1, 0, 4])  # false
print can_jump3([2, 3, 1, 1, 4])  # true
print can_jump3([3, 2, 1, 0, 4])  # false
