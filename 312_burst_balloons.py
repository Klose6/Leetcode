"""
312 burst balloons
"""

class Solution(object):
	def max_scores(self, nums):
		if not nums:
			return 0
		nums = [1]+nums+[1]
		n = len(nums)
		dp = [[0] * n for _ in xrange(n)]
		for l in xrange(2, n):
			for i in xrange(0, n-l):
				j = i+l
				for k in xrange(i+1, j):
					dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[j]*nums[k])
		return dp[0][n-1]
s=Solution()
print s.max_scores([3,1,5,8]) #167