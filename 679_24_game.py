"""
24 game
"""
#import math #math.isclose() is not in 2.7
import itertools


class Solution(object):
	def judge_point_24(self, nums):
		if not nums:
			return False
		if len(nums) == 1:
			return abs(nums[0]-24)<0.0001
		return any(self.judge_point_24([x]+list(p)[2:])
							for p in itertools.permutations(nums) #permutations return a list of tuples
							for x in [p[0]+p[1],p[0]-p[1],
												p[0]*p[1], p[1] and float(p[0])/p[1]])
s=Solution()
print s.judge_point_24([4,1,8,7]) #True
print s.judge_point_24([1,2,1,2]) #False