"""
340 Longest substring with at most k distinct characters
http://www.cnblogs.com/grandyang/p/5351347.html
"""

class Solution(object):
	def get_longest_k_distinct(self, s, k):
		if not s: return 0
		count = {}
		res, left = 0, 0
		for i in range(len(s)):
			count[s[i]] = count[s[i]]+1 if s[i] in count else 1
			while len(count) > k:
				count[s[left]] -= 1
				if count[s[left]] == 0:
					del count[s[left]]
				left += 1
			res = max(res, i-left+1)
		return res


class Solution1:
	def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
		if not s or k <= 0: return 0
		res = 0
		start = 0
		d = [0] * 128
		num = 0
		for i, c in enumerate(s):
			if d[ord(c)] == 0: num += 1
			d[ord(c)] += 1
			while num > k:
				d[ord(s[start])] -= 1
				if d[ord(s[start])] == 0:
					num -= 1
				start += 1
			res = max(res, i - start + 1)
		return res


s = Solution()
print(s.get_longest_k_distinct("eceba", 2)) # 3