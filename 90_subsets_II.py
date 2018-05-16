"""
90 subsets II
if nums[i] == nums[i-1], then no need to add it to all of the previous subset,
only add it to the last l subsets
"""


def subsets_wit_duplicates(nums):
	if not nums:
		return []
	res = [[]]
	nums.sort()
	l = 0
	for i in range(len(nums)):
		if i == 0 or nums[i] != nums[i - 1]:
			l = len(res)
		for j in range(len(res) - l, len(res)):
			res.append(res[j] + [nums[i]])
	return res


print subsets_wit_duplicates([1, 2, 2])
