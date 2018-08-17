"""
215 kth largest element in an array
"""
from heapq import heappush, heappop


def find_kth_largest(nums, k):
	pq = []
	for i, v in enumerate(nums):
		heappush(pq, v)
		if i >= k:
			heappop(pq)
	return heappop(pq)


print find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
print find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
