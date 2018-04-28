"""
46 permutations
"""
import itertools


def permutations(nums):
	return [[n] + p
					for i, n in enumerate(nums)
					for p in permutations(nums[:i] + nums[i + 1:])] or [[]]


def permutations2(nums):
	return list(itertools.permutations(nums))


print permutations([1, 2, 3])
