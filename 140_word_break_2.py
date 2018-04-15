"""
140 word break II
"""
import copy

class Solution(object):
	def wordbreak(self,s,dic):
		if not s or not dic:
			return
		res = []
		def helper(s, start, curlist):
			if start==len(s):
				print curlist
				res.append(copy.deepcopy(curlist))
				return
			for i in range(start+1, len(s)+1):
				if s[start: i] in dic:
					# print s[start:i]
					curlist.append(s[start:i])
					helper(s, i, curlist)
					curlist.pop()
		helper(s, 0, [])
		return res
	def wordbreak2(self, s, dic):
		mem={len(s): [""]}
		def sentences(i):
			if i not in mem:
				mem[i] = [s[i:j] + (tail and " "+tail)
									for j in range(i+1, len(s)+1)
									if s[i:j] in dic
									for tail in sentences(j)]
			return mem[i]
		return sentences(0)
s=Solution()
dic=["cat","cats","and","sand","dog"]
print s.wordbreak("catsanddog", dic)
print s.wordbreak2("catsanddog", dic)
