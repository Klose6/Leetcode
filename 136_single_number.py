"""
136 single number
"""
import operator


def single_number(nums):
	res = 0
	for n in nums:
		res ^= n
	return res


def single_number1(nums):
	return 2 * sum(set(nums)) - sum(nums)


def single_number2(nums):
	return reduce(operator.xor, nums)


print single_number([2, 2, 1]) == 1
print single_number1([2, 2, 1]) == 1
print single_number2([2, 2, 1]) == 1
