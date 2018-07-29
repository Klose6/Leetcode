"""
78 subsets
"""


def subsets(nums):
	if not nums:
		return []
	res = []
	dfs(nums, 0, [], res)
	return res


def dfs(nums, start, cur, res):
	res.append(cur)
	for i in range(start, len(nums)):
		dfs(nums, i + 1, cur + [nums[i]], res)


def subsets2(nums):
	res = [[]]
	for num in nums:
		res += [item + [num] for item in res]
	return res


print subsets([1, 2, 3])
print subsets2([1, 2, 3])
