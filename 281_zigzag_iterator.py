"""
281 ZigZag Iterator
http://www.cnblogs.com/grandyang/p/5212785.html
"""
import collections

class Solution(object):
	def __init__(self, a, b):
		self.q = collections.deque((len(v), iter(v)) for v in (a, b) if v)
	def next(self):
		len, iter = self.q.popleft()
		if len > 1: # add it to the queue only when its len > 1
			self.q.append((len-1, iter))
		return next(iter)
	def hasNext(self):
		return bool(self.q)

s = Solution([1,2], [3,4,5,6])
for i in xrange(6):
	print s.next()
