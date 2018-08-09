"""
198 house robber
"""


def rob(nums):
	n = len(nums)
	dp = [0] * n
	dp[0], dp[1] = nums[0], max(nums[0], nums[1])
	for i in range(n)[2:]:
		dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
	return dp[n - 1]


def rob1(nums):
	last, now = 0, 0
	for i in nums:
		last, now = now, max(last + i, now)
	return now


print rob([1, 2, 3, 1]) == 4
print rob1([1, 2, 3, 1]) == 4
