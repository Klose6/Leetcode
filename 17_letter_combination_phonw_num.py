"""
17 letter combination of a phone number
"""
import itertools


class Solution(object):
	def letter_combinations(self, digits):
		if not digits:
			return []
		M = {"2": "abc", "3": "def", "4": "ghi", "5": "jki", "6": "mno",
				 "7": "pqrs", "8": "tuv", "9": "wxyz"}
		# ret = [""]
		# for d in digits:
		# 	tmp = []
		# 	for a in ret:
		# 		for b in M[d]:
		# 			tmp.append(a+b)
		# 	ret = tmp
		return reduce(lambda acc, digit: [x + y for x in acc for y in M[digit]], digits, [''])

	# groups = [M[d] for d in digits]
	# return ["".join(x) for x in itertools.product(*groups)]


s = Solution()
print s.letter_combinations("23")
