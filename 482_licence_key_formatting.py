"""
482 Licence key formatting
https://leetcode.com/problems/license-key-formatting/discuss/96497/Python-solution
"""

class Solution(object):
	def licenceKeyFormatting(self, s, k):
		if not s or not k:
			return
		res = []
		n = len(s)
		for i in xrange(n-1, -1, -1):
			if s[i] == "-":
				continue
			res.append(s[i].upper())
			if len(res) % (k+1) == k and i > 0:
				res.append("-")
		return "".join(res[::-1])

	def licenceKeyFormatting2(self, s, k):
		if not s or not k:
			return
		s = s.replace("-", "")
		n = len(s)
		i = k if n%k == 0 else n%k
		res = [s[:i]]
		while i < n:
			res.append(s[i:i+k].upper())
			i += k
		return "-".join(res)

s = Solution()
print s.licenceKeyFormatting("5F3Z-2e-9-w", 4)
print s.licenceKeyFormatting("2-5g-3-2", 2)

print s.licenceKeyFormatting2("5F3Z-2e-9-w", 4)
print s.licenceKeyFormatting2("2-5g-3-2", 2)