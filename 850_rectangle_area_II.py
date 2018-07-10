"""
850 rectangle area II

"""


class Solution(object):
	def rectangle_area(self, rectangles):
		# using segment tree
		OPEN, CLOSE = 1, -1
		events = []
		X = set()
		for x1, y1, x2, y2 in rectangles:
			events.append((y1, OPEN, x1, x2))
			events.append((y2, CLOSE, x1, x2))
			X.add(x1)
			X.add(x2)
		events.sort()
		X = sorted(X)
		Xi = {x: i for i, x in enumerate(X)}
		st = SegmentTreeNode(0, len(X) - 1)
		cur_y = events[0][0]
		cur_x_sum = area = 0
		for y, sign, x1, x2 in events:
			area += (y - cur_y) * cur_x_sum
			cur_x_sum = st.update(X, Xi[x1], Xi[x2], sign)
			cur_y = y
		return area % (10 ** 9 + 7)


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


print Solution().rectangle_area([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]])  # 6
