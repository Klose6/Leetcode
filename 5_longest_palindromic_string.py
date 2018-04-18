"""
5 longest palindromic string
"""


class Solution(object):
	def longest_palindrome(self, s):
		if not s or len(s) < 2:
			return s

		def extend(s, l, r):
			while l >= 0 and r < len(s) and s[l] == s[r]:
				l -= 1
				r += 1
			return l + 1, max(r - l - 1, 0)

		if not s:
			return
		res, res_len = "", 0
		for i in range(len(s)):
			l, le = extend(s, i, i)
			if le > res_len:
				res, res_len = s[l:l + le], le
			l, le = extend(s, i, i + 1)
			if le > res_len:
				res, res_len = s[l:l + le], le
		return res


s = Solution()
print s.longest_palindrome("babad")  # bab
print s.longest_palindrome("cbbd")  # bb
