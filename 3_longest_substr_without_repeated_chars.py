"""
3 Longest substring without repeating characters
"""


class Solution(object):
	def get_longest_substr(self, s):
		# O(n)
		if not s:
			return
		map = {}
		max_len, res = 0, None
		start = 0
		for i, v in enumerate(s):
			if v in map:
				start = map.get(v) + 1
			if i - start + 1 > max_len:
				max_len = i - start + 1
				res = s[start:i + 1]
			map[v] = i
		return res


s = Solution()
print s.get_longest_substr("abcabcbb")  # abc
print s.get_longest_substr("pwwke")  # wke
