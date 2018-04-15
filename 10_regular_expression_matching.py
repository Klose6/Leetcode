"""
10 regular expression matching
"""

class Solution(object):
	def reg_match(self, s, p):
		if not p:
			return not s
		if len(p) == 1:
			return len(s) == 1 and s[0]==p[0] or p[0]=="."
		if p[1] != "*":
			return s and (s[0] == p[0] or p[0] == ".") and \
			self.reg_match(s[1:], p[1:])
		while s and s[0]==p[0] or p[0]==".":
			if self.reg_match(s, p[2:]):
				return True
			s=s[1:]
		return self.reg_match(s, p[2:])
	def reg_match2(self, s, p):
		m,  n = len(s), len(p)
		dp = [[False]*(m+1) for _ in range(n+1)]
		dp[0][0] = True
		for i in range(1, n):
			if p[i] == "*":
				dp[i+1][0] = dp[i-1][0]
		for i in range(n):
			for j in range(m):
				if p[i] == "*":
					dp[i+1][j+1] = dp[i-1][j+1] or dp[i][j+1]
					if p[i-1]==s[j] or p[i-1] == ".":
						dp[i+1][j+1] |= dp[i+1][j]
				else:
					dp[i+1][j+1] = dp[i][j] and (s[j]==p[i] or p[i] == ".")
		return dp[-1][-1]

s=Solution()
print s.reg_match2("aa", "a") #False
print s.reg_match2("aa", "aa") #True
print s.reg_match2("aab", "c*a*b*") # True