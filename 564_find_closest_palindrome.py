"""
564 find closest palindrome
"""


class Solution(object):
	def find_closest_palindrome(self, s):
		def delta(a, b):
			return abs(int(a) - int(b))

		n = len(s)
		potentials = [str(i) for m in (n, n - 1) for i in (10 ** m + 1, 10 ** m - 1)]
		prefix = s[:(n + 1) / 2]
		p = int(prefix)
		for start in map(str, (p - 1, p, p + 1)):
			potentials.append(start + (start[:-1] if n % 2 else start)[::-1])
		res = None
		for p in potentials:
			if p != s and not p.startswith("00"):
				if (res is None or delta(res, s) > delta(p, s)) \
						or (delta(res, s) == delta(p, s) and int(p) < int(res)):
					res = p
		return res


print Solution().find_closest_palindrome("123") == "121"
