"""
346 Moving average from data stream
http://www.cnblogs.com/grandyang/p/5450001.html
"""

class Solution(object):
	def __init__(self, size):
		self.size = size
		self.nums = []
	def next(self, num):
		self.nums.append(num)
		while len(self.nums) > self.size:
			self.nums.pop(0)
		return sum(self.nums) / len(self.nums)

s = Solution(3)
print s.next(1)
print s.next(2)
print s.next(3)
print s.next(4)