"""
155 min stack
"""


class MinStack(object):
	def __init__(self):
		self.stack = []

	def push(self, x):
		cur_min = self.getMin()
		if not cur_min or x < cur_min:
			cur_min = x
		self.stack.append((x, cur_min))

	def pop(self):
		if not self.stack:
			return None
		return self.stack.pop()

	def top(self):
		if not self.stack:
			return None
		return self.stack[-1][0]

	def getMin(self):
		if not self.stack:
			return None
		return self.stack[-1][1]
