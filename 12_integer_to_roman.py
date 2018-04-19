"""
12 integer to Roman
"""


class Solution(object):
	def integer_to_roman(self, num):
		I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
		X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
		C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
		M = ["", "M", "MM", "MMM"]
		return M[num / 1000] + C[num % 1000 / 100] + X[num % 100 / 10] + I[num % 10]


s = Solution()
print s.integer_to_roman(58)  # LVIII
