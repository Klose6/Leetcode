"""
316 remove duplicate letters
"""

class Solution(object):
	def remove_duplicates(self, s):
		if not s:
			return
		rindex={c:i for i, c in enumerate(s)}
		res = ""
		for i in s:
			if i not in res:
				while i < res[-1:] and rindex[i] < rindex[res[-1]]:
					res=res[:-1]
				res+=i
		return res
s=Solution()
print s.remove_duplicates("bcabc") #abc
print s.remove_duplicates("cbacdcbc") #acdb