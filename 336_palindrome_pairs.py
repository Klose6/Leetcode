"""
336 palindromes pairs
"""

class Solution(object):
	def ispalindrome(self, s):
		return s == s[::-1]
	def get_palindrome_pairs(self, words):
		res = []
		if not words:
			return res
		idx_dic = {word:i for i, word in enumerate(words)}
		for idx, w in enumerate(words):
			for i in range(len(w)+1):
				left, right=w[:i], w[i:]
				reverse_left, reverse_right = left[::-1],right[::-1]
				if self.ispalindrome(left) and reverse_right != w and reverse_right in words:
					# idx1 = words.index(reverse_right)
					idx1=idx_dic[reverse_right]
					res.append((idx1, idx))
				if i != len(words) and self.ispalindrome(right) and\
								reverse_left != w and reverse_left in words:
					# idx2 = words.index(reverse_left)
					idx2=idx_dic[reverse_left]
					res.append((idx, idx2))
		return res
s=Solution()
print s.get_palindrome_pairs(["bot", "t", "to"])