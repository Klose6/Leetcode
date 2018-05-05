""""
69 sqrt(x)
"""
import sys


def sqrt(x):
	if not x:
		return 0
	lo, hi = 0, sys.maxint
	while True:
		mid = lo + (hi - lo) / 2
		if mid > x / mid:
			hi = mid - 1
		else:
			if mid + 1 > x / (mid + 1):
				return mid
			else:
				lo = mid + 1


def sqrt1(x):
	# Newton method
	r = x
	while r * r > x:
		r = (r + x / r) / 2
	return r


print sqrt(8)
print sqrt1(8)
