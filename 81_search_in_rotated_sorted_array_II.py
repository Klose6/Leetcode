"""
81 search in rotated sorted array II
"""


def search(nums, target):
	if not nums:
		return False
	lo, hi = 0, len(nums) - 1
	while lo < hi:
		mid = lo + (hi - lo) / 2
		if nums[mid] == target:
			return True
		if nums[mid] < nums[hi]:
			if nums[mid] < target <= nums[hi]:
				lo = mid + 1
			else:
				hi = mid - 1
		elif nums[mid] > nums[hi]:
			if nums[lo] <= target < nums[mid]:
				hi = mid - 1
			else:
				lo = mid + 1
		else:
			hi -= 1
	return False


print search([2, 5, 6, 0, 0, 1, 2], 0)  # true
print search([2, 5, 6, 0, 0, 1, 2], 3)  # false
