"""
39 combination sum
"""


def combination_sum(nums, target):
	if not nums:
		return
	nums = sorted(nums)
	dp = [[[]]] + [[] for _ in range(target)]
	for i in range(1, target + 1):
		for num in nums:
			if num > i:
				break
			for j in dp[i - num]:
				if not j or num >= j[-1]:
					dp[i].append(j + [num])
	return dp[target]


def combination_sum2(nums, target):
	nums = sorted(nums)
	res = []

	def dfs(cur_res, cur_sum):
		if cur_sum == target:
			res.append(cur_res)
			return
		for num in nums:
			if num + cur_sum > target:
				break
			if not cur_res or num >= cur_res[-1]:
				dfs(cur_res + [num], cur_sum + num)

	dfs([], 0)
	return res


print combination_sum([2, 3, 6, 7], 7)
print combination_sum2([2, 3, 6, 7], 7)
print combination_sum([2, 3, 5], 8)
print combination_sum2([2, 3, 5], 8)
