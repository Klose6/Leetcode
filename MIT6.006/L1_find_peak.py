"""
find the peak element from array, matrix
"""


def find_peak_array(nums):
	"""
	Find the peak element from the array
	using binary search, O(log(n))
	"""
	if not nums:
		return
	return find_helper(nums, 0, len(nums) - 1)


def find_helper(nums, lo, hi):
	"""
	Helper function to find the peak in the array
	"""
	if lo > hi:
		return
	if lo == hi:
		return nums[lo]
	l, mid = len(nums), lo + (hi - lo) // 2
	if mid < l - 1 and nums[mid] < nums[mid + 1]:
		return find_helper(nums, mid + 1, hi)
	elif mid > 0 and nums[mid] < nums[mid - 1]:
		return find_helper(nums, lo, mid - 1)
	else:
		return nums[mid]


def find_peak_2D(matrix):
	"""
	1. Greedy Ascent Algorithm O(m*n)
	2. Use binary search on all the columns and find the global maximum for the column to check. O(n*log(m))
	"""
	if not matrix:
		return
	return find_peak_2D_helper(matrix, 0, len(matrix) - 1)


def find_peak_2D_helper(matrix, lo, hi):
	m, n = len(matrix), len(matrix[0])
	mid = lo + (hi - lo) // 2
	idx, cur_max = find_array_max(matrix[mid])
	if lo == hi:
		return cur_max
	if mid > 0 and matrix[mid][idx] < matrix[mid - 1][idx]:
		return find_peak_2D_helper(matrix, lo, mid - 1)
	elif mid < m - 1 and matrix[mid][idx] < matrix[mid + 1][idx]:
		return find_peak_2D_helper(matrix, mid + 1, hi)
	else:
		return cur_max


def find_array_max(array):
	idx, cur_max = 0, array[0]
	for i, v in enumerate(array):
		if v > cur_max:
			idx, cur_max = i, v
	return idx, cur_max


# testing
assert find_peak_array([1]) == 1
assert find_peak_array([1, 2]) == 2

assert find_peak_2D([
	[1, 2, 3],
	[4, 5, 6]
]) == 6

assert find_peak_2D([
	[1, 2, 3],
	[4, 7, 6]
]) == 7
