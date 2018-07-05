"""
857 minimum cost to hire k workers

wage[i] : wage[j] = quality[i] : quality[j]
So we have wage[i] : quality[i] = wage[j] : quality[j]
We pay wage to every worker in the group with the same ratio compared to his own quality.
"""
import heapq


class Solution(object):
	def min_cost(self, quality, wage, k):
		ratios = sorted([(float(w) / q, q) for w, q in zip(wage, quality)])
		qsum = 0
		res = float("inf")
		heap = []
		for ratio, q in ratios:
			heapq.heappush(heap, -q)
			qsum += q
			if len(heap) > k:
				qsum += heapq.heappop(heap)
			if len(heap) == k:
				res = min(res, ratio * qsum)
		return res


print Solution().min_cost([10, 20, 5], [70, 50, 30], 2)  # 105
