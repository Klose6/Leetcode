"""
8 string to integer
"""


class Solution(object):
	def str_to_int(self, s):
		if not s:
			return 0
		ls = list(s.strip())
		sign = -1 if ls[0] == "-" else 1
		if ls[0] in ("-", "+"):
			del ls[0]
		ret, i = 0, 0
		while i < len(ls) and ls[i].isdigit():
			ret = ret * 10 + ord(ls[i]) - ord("0")
			i += 1
		return max(-2 ** 31, min(2 ** 31, sign * ret))


s = Solution()
print s.str_to_int("123")
print s.str_to_int("  -42")
print s.str_to_int("123 with ")
print s.str_to_int("-91283472332")
