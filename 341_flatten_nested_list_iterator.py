"""
341 flatten nested list iterator
"""

class Solution(object):
	def __init__(self, nestedlist):
		self.stack = nestedlist[::-1]

	def next(self):
		return self.stack.pop()

	def hasnext(self):
		while self.stack:
			top = self.stack[-1]
			if not isinstance(top, list):
				return True
			self.stack = self.stack[:-1]+top[::-1]
		return False
s= Solution([[1,2],2,[1,1]])
while s.hasnext():
	print s.next()