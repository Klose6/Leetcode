"""
169 majority element
"""


def majority_element(nums):
	res, count = nums[0], 1
	for n in nums[1:]:
		if count == 0:
			count += 1
			res = n
		elif res == n:
			count += 1
		else:
			count -= 1
	return res


print majority_element([3, 2, 3]) == 3
