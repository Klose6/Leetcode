"""
Segment Tree
"""


class SegmentTreeNode(object):
	def __init__(self, start, end):
		self.start, self.end = start, end
		self.total = self.count = 0
		self._left = self._right = None

	def mid(self):
		return (self.start + self.end) / 2

	def left(self):
		self._left = self._left or SegmentTreeNode(self.start, self.mid())
		return self._left

	def right(self):
		self._right = self._right or SegmentTreeNode(self.mid(), self.end)
		return self._right

	def update(self, X, i, j, val):
		if i >= j:
			return 0
		if self.start == i and self.end == j:
			self.count += val
		else:
			self.left().update(X, i, min(self.mid(), j), val)
			self.right().update(X, max(self.mid(), i), j, val)
		if self.count > 0:
			self.total = X[self.end] - X[self.start]
		else:
			self.total = self.left().total + self.right().total
		return self.total
