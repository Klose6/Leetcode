"""
458 Poor Pigs
https://leetcode.com/problems/poor-pigs/discuss/94266
"""

class Solution(object):
	def poor_pigs(self, buckets, minuteToDie, minuteToTest):
		if not buckets or minuteToDie <= 0 or minuteToTest <=0:
			return 0
		pigs = 0
		while ( minuteToTest // minuteToDie + 1) ** pigs <= buckets:
			pigs += 1
		return pigs

print(Solution().poor_pigs(1000, 15, 60))