"""
418 Sentence screen fitting
http://www.cnblogs.com/grandyang/p/5975426.html
"""

class Solution(object):
	def sentenceFitting(self, words, r, c):
		if not s or not c or not r:
			return
		all = " ".join(words) + " "
		n = len(all)
		start = 0
		for i in xrange(r):
			start += c
			if all[start % n] == " ":
				start += 1
			else:
				while start>0 and all[(start-1)%n] != " ":
					start -= 1
		return start / n
	def sentenceFitting2(self, words, r, c):
		if not words or not r or not c:
			return
		all = " ".join(words) + " "
		n = len(all)
		idx = 0
		res = 0
		for i in xrange(r):
			colsRemain = c
			while colsRemain > 0:
				if len(words[idx]) <= colsRemain:
					colsRemain -= len(words[idx])
					if colsRemain > 0:
						colsRemain -= 1
					idx += 1
					if idx >= len(words):
						res += (1 + colsRemain / n)
						colsRemain %= n
						idx = 0
				else:
					break
		return res

s = Solution()
print s.sentenceFitting(["hello", "world"], 2, 8) #1
print s.sentenceFitting2(["hello", "world"], 2, 8) #1
