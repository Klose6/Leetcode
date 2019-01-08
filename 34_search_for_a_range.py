"""
34 search for a range
"""
import bisect

def search_for_range(nums, target):
	res = [-1, -1]
	if not nums:
		return res
	l, r = 0, len(nums) - 1
	# search for the left one
	while l < r:
		mid = l + (r - l) / 2
		if nums[mid] >= target:
			r = mid
		else:
			l = mid + 1
	if nums[l] != target:
		return res
	res[0] = l
	# search for the right one
	r = len(nums) - 1
	while l < r:
		# make mid have bias toward right
		mid = l + (r - l) / 2 + 1
		if nums[mid] <= target:
			l = mid
		else:
			r = mid - 1
	res[1] = r
	return res


def search_for_range2(nums, target):
	res = [-1, -1]
	if not nums:
		return res
	lo = bisect.bisect_left(nums, target)
	return [lo, bisect.bisect(nums, target) - 1] if target in nums[lo:lo + 1] else res


def search_for_range3(nums, target):
	if not nums:
		return [-1, -1]

	def find_left():
		idx = -1
		lo, hi = 0, len(nums) - 1
		while lo <= hi:
			mid = lo + (hi - lo) / 2
			if nums[mid] < target:
				lo = mid + 1
			else:
				hi = mid - 1
			if nums[mid] == target:
				idx = mid
		return idx

	def find_right():
		idx = -1
		lo, hi = 0, len(nums) - 1
		while lo <= hi:
			mid = lo + (hi - lo) / 2
			if nums[mid] <= target:
				lo = mid + 1
			else:
				hi = mid - 1
			if nums[mid] == target:
				idx = mid
		return idx

	return [find_left(), find_right()]


assert search_for_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]  # [3,4]
assert search_for_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

assert search_for_range2([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert search_for_range2([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

assert search_for_range3([5, 7, 7, 8, 8, 10], 8) == [3, 4]  # [3,4]
assert search_for_range3([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
