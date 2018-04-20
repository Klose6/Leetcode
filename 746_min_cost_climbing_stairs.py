"""
746 min cost climbing stairs
"""


def min_cost(cost):
	# Min cost to reach step i is the min of costs to reach it from [i-1] and [i-2].
	if not cost:
		return 0
	n = len(cost)
	if n == 0 or n == 1:
		return 0
	cost0, cost1 = cost[0], cost[1]
	for i in range(2, n):
		cost0, cost1 = cost1, min(cost0, cost1) + cost[i]
	return min(cost0, cost1)


print min_cost([10, 15, 20])  # 15
print min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])  # 6
