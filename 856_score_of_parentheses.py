"""
856 score of parentheses
"""
import itertools


class Solution(object):
	def scores(self, s):
		res = layers = 0
		for a, b in itertools.izip(s, s[1:]):
			layers += 1 if a == "(" else -1
			if a + b == "()":
				res += 2 ** (layers - 1)
		return res


print Solution().scores("(()(()))")  # 6
