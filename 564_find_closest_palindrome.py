"""
564 find closest palindrome
"""


class Solution(object):
	def find_closest_palindrome(self, s):
		def delta(a, b):
			return abs(int(a) - int(b))

		n = len(s)
		potentials = [str(i) for m in (n, n - 1) for i in (10 ** m + 1, 10 ** m - 1)]
    prefix = s[:(n + 1) // 2]
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

	def find_closest_palindrome1(self, s):
    """
    Find the potential candidates, if the final answer has the same length as the input number,
    then the answer must be the middle digits +1, +0 or -1 then flipped into a palindrome
    if the answer has a different length of digits, then it must be has the form of 99...99 or 10...01
    """
		n = len(s)
    potentials = {str(10 ** n - 1), str(10 ** (n - 1) + 1)}
    prefix = int(s[:(n + 1) // 2])
		for i in map(str, (prefix - 1, prefix, prefix + 1)):
			potentials.add(i + [i, i[:-1]][n % 2][::-1])
		potentials.discard(s)
    min_val = min(potentials, key=lambda x: abs(int(x) - int(s)))
    print(min_val)
    return min_val


assert Solution().find_closest_palindrome("123") == "121"
assert Solution().find_closest_palindrome1("123") == "121"
