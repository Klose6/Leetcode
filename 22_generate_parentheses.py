"""
22 generate parentheses
"""


class Solution(object):
	def generate_parentheses(self, n):
		if n <= 0:
			return []
		res = []

		def dfs(cur_s, open, close):
			if open == n and close == n:  # len(cur_s) == 2*n:
				res.append(cur_s)
				return
			if open < n:
				dfs(cur_s + "(", open + 1, close)
			if close < open:
				dfs(cur_s + ")", open, close + 1)

		dfs("", 0, 0)
		return res


s = Solution()
print s.generate_parentheses(3)
