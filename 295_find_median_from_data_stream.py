"""
295 find median from data stream
"""
from Queue import PriorityQueue
from heapq import *

class Solution(object):
	def __init__(self):
		self.maxheap = [] #riorityQueue()
		self.minheap =[] # PriorityQueue()
	def add_num(self, num):
		heappush(self.maxheap, num)
		if len(self.maxheap) > len(self.minheap):
			heappush(self.minheap, -heappop(self.maxheap))
	def find_median(self):
		if (len(self.maxheap) + len(self.minheap))/2:
			return (self.maxheap[0]-self.minheap[0])/2.0
		else:
			return -self.minheap[0]
s=Solution()
s.add_num(1)
print s.find_median()
s.add_num(2)
print s.find_median()