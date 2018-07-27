"""
630 course schedule III
"""
from heapq import heappush, heappop


class Solution(object):
	def course_schedule(self, courses):
		s = []
		start = 0
		for t, end in sorted(courses, key=lambda x: x[1]):
			start += t
			heappush(s, -t)  # max heap
			if start > end:  # the newly pushed t may also be pope
				start += heappop(s)
		return len(s)


print Solution().course_schedule([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3
