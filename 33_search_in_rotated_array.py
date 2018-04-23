"""
33 search in rotated array
"""


def search_rorated_array(nums, target):
	if not nums:
		return
	n = len(nums)
	l, r = 0, n - 1
	# find the index of the smallest value
	while l < r:
		mid = l + (r - l) / 2
		if nums[mid] > nums[r]:
			l = mid + 1
		else:
			r = mid
	# print "smallest: " + str(l)
	## l==r is the index of the smallest value
	rotation = l
	l, r = 0, n - 1
	while l <= r:
		mid = l + (r - l) / 2
		real_mid = (mid + rotation) % n
		# print "mid: " + str(mid)
		if nums[real_mid] == target:
			return real_mid
		elif nums[real_mid] > target:
			r = mid - 1
		else:
			l = mid + 1
	return -1


print search_rorated_array([4, 5, 6, 7, 0, 1, 2], 0)  # 4
print search_rorated_array([4, 5, 6, 7, 0, 1, 2], 3)  # -1
