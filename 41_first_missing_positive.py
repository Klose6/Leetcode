"""
41 first missing positive
"""


def find_first_missing_positve(nums):
	if not nums:
		return 1
	n = len(nums)
	for i in range(n):
		while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
			# print nums
			tmp = nums[nums[i] - 1]
			nums[nums[i] - 1] = nums[i]
			nums[i] = tmp
	for i in range(n):
		if nums[i] != i + 1:
			return i + 1
	return n + 1


print find_first_missing_positve([1, 2, 0])  # 3
print find_first_missing_positve([3, 4, -1, 1])  # 2
