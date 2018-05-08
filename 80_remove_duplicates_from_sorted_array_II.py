"""
80 remove duplicates from sorted array II
"""


def remove_duplicates(nums):
	if not nums:
		return -1
	i = 0
	for n in nums:
		if i < 2 or n > nums[i - 2]:
			nums[i] = n
			i += 1
	return i
