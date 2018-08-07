"""
152 maximum product subarray
"""
import sys


def max_product_subarray(nums):
	res = imax = imin = nums[0]
	for n in nums[1:]:
		if n < 0:
			imax, imin = imin, imax
		imax = max(n, imax * n)
		imin = min(n, imin * n)
		res = max(res, imax)
	return res


print max_product_subarray([-1, 0, -2]) == 0
print max_product_subarray([2, 3, -2, 4]) == 6
