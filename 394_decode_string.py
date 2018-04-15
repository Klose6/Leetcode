"""
394 decode string
"""
import re
class Solution(object):
	def decodestring(self, s):
		while "[" in s:
			s = re.sub(r"(\d+)\[([a-z]*)\]", lambda m:int(m.group(1))*m.group(2), s)
		return s
	def helper(self, p, i, j):
		print i,j
		if not p:
			return ""
		res = ""
		while i < j:
			if not p[i].isdigit():
				res += p[i]
				i+=1
			else:
				num = 0
				while i<j and p[i].isdigit():
					num = num*10 + int(p[i])
					i+=1
				left=1
				i+=1
				k =i
				while k<j and left>0:
					if p[k] == "[":
						left+=1
					elif p[k] == "]":
						left-=1
					k+=1
				k-=1
				substr = self.helper(p, i, k)
				res += substr*num
				i = k + 1
		return res
	def decodestring2(self, p):
		return self.helper(p, 0, len(p))
	def decodestring3(self, p):
		if not p:
			return ""
		curstring = ""
		num = 0
		stack = []
		for i in p:
			if i == "[":
				stack.append(curstring)
				stack.append(num)
				curstring= ""
				num = 0
			elif i == "]":
				num = stack.pop()
				prestring = stack.pop()
				curstring = prestring + curstring*num
			elif i.isdigit():
				num = num*10 + int(i)
			else:
				curstring += i
		return curstring

s = Solution()
# print s.decodestring("3[abc]")
# print s.decodestring("3[a2[c]]")
# print s.decodestring2("3[abc]")
# print s.decodestring2("3[a2[c]]")
print s.decodestring3("3[abc]")
print s.decodestring3("3[a2[c]]")