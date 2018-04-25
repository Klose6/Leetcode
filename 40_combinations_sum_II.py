"""
40 combinations sum II
"""


def combinations_sum(nums, target):
	if not nums:
		return []
	nums = sorted(nums)
	res = []
	dfs(nums, 0, [], target, res)
	return res


def dfs(nums, start, cur, left, res):
	if not left:
		res.append(cur)
	for i in range(start, len(nums)):
		if i > start and nums[i] == nums[i - 1]:
			continue
		if nums[i] > left:
			break
		dfs(nums, i + 1, cur + [nums[i]], left - nums[i], res)


def combinations_sum2(nums, target):
	if not nums:
		return []
	nums.sort()
	dp = [set() for _ in range(target + 1)]
	dp[0].add(())
	for n in nums:
		for j in range(target, n - 1, -1):  # need to be in reverse order
			for prev in dp[j - n]:
				dp[j].add(prev + (n,))
	return list(dp[-1])


print combinations_sum([10, 1, 2, 7, 6, 1, 5], 8)
print combinations_sum2([10, 1, 2, 7, 6, 1, 5], 8)
