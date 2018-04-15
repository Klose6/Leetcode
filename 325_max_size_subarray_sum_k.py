"""
maximum size subarray sum equals to k
Given an array nums and a target value k, find the maximum length of a
subarray that sums to k. If there isn't one, return 0 instead.
https://discuss.leetcode.com/topic/33259/o-n-super-clean-9-line-java-solution-with-hashmap
https://discuss.leetcode.com/topic/33331/clean-python-solution-one-pass
"""


def max_subarray_sumk(nums, k):
	if not nums:
		return 0
	map = {}
	sum, max = 0, 0
	for i, val in enumerate(nums):
		sum += val
		if sum == k:
			max = i+1
		elif sum-k in map:
			max = max(max, i-map.get(sum-k))
		if not map.get(sum):
			map[sum] = i
	return max

