"""
121 best time to buy and sell stock
"""
import sys


def maxProfit(prices):
	if not prices or len(prices) < 2:
		return 0
	res = 0
	m = sys.maxint  # max int for python2
	for p in prices:
		m = min(m, p)
		res = max(p - m, res)
	return res


print maxProfit([7, 1, 5, 3, 6, 4]) == 5
