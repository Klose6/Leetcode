"""
340 Longest substring with at most k distinct characters
http://www.cnblogs.com/grandyang/p/5351347.html
"""

class Solution(object):
	def get_longest_k_distinct(self, s, k):
		if not s:
			return 0
		count = {}
		res, left = 0, 0
		for i in xrange(len(s)):
			count[s[i]] = count[s[i]]+1 if s[i] in count else 1
			while len(count) > k:
				count[s[left]] -= 1
				if count[s[left]] == 0:
					del count[s[left]]
				left += 1
			res = max(res, i-left+1)
		return res

s = Solution()
print s.get_longest_k_distinct("eceba", 2) # 3