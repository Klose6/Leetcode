"""
215 kth largest element in an array
"""
import random
from heapq import heappush, heappop


def find_kth_largest(nums, k):
	pq = []
	# print nums
	# randomize(nums)
	# print nums
	# random.shuffle(nums)
	for i, v in enumerate(nums):
		heappush(pq, v)
		if i >= k:
			heappop(pq)
	return heappop(pq)


def randomize(a):
	for i in range(len(a)):
		pos = random.randint(0, i)
		a[i], a[pos] = a[pos], a[i]


print find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
print find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
