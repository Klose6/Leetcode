"""
139 word break
"""


def word_break(s, dic):
	n = len(s)
	dp = [False] * (n + 1)
	dp[0] = True
	for i in range(1, n + 1):
		for j in range(0, i):
			if dp[j] and s[j:i] in dic:
				dp[i] = True
				break
	return dp[n]


print word_break("goodluck", ["good", "luck"]) == True
