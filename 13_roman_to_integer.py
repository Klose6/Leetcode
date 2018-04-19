"""
13 Roman to integer
"""


class Solution(object):
	def roman_to_int(self, r):
		if not r:
			return 0
		res = 0
		for s in r[::-1]:
			if s == "I":
				res += -1 if res >= 5 else 1
			elif s == "V":
				res += 5
			elif s == "X":
				res += 10 * (-1 if res >= 50 else 1)
			elif s == "L":
				res += 50
			elif s == "C":
				res += 100 * (-1 if res >= 500 else 1)
			elif s == "D":
				res += 500
			elif s == "M":
				res += 1000
		return res

	def roman_to_int2(self, r):
		M = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
		res = M[r[-1]]
		for i in range(len(r) - 1)[::-1]:
			if M[r[i]] < M[r[i + 1]]:
				res -= M[r[i]]
			else:
				res += M[r[i]]
		return res


s = Solution()
print s.roman_to_int("III")  # 3
print s.roman_to_int("MCMXCIV")  # 1994
print s.roman_to_int2("III")  # 3
print s.roman_to_int2("MCMXCIV")  # 1994
