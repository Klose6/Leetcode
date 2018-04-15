"""
224 basic calculator
"""

class Solution(object):
	def calclulate(self, s):
		if not s:
			return 0
		sign, res = [1, 1], 0
		i, n = 0, len(s)
		while i < n:
			if s[i].isdigit():
				start = i
				while i<n and s[i].isdigit():
					i+=1
				res += sign.pop() * int(s[start:i])
				continue
			if s[i] in "+-(":
				sign.append(sign[-1] * (1, -1)[s[i] == "-"])
			elif s[i] == ")":
				sign.pop()
			i+=1
		return res
s=Solution()
print s.calclulate("3-(2+(9-4))")
print s.calclulate("-1")