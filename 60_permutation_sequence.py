"""
60 permutation sequence

for permutation, the 1st (n-1)! starts with 1, next (n-1)! ones
starts wth 2
"""
import math


def get_permutation(n, k):
	numbers = range(1, n + 1)
	permutations = []
	k -= 1
	while n > 0:
		n -= 1
		idx, k = divmod(k, math.factorial(n))
		permutations.append(str(numbers[idx]))
		numbers.remove(numbers[idx])
	return "".join(permutations)


print get_permutation(3, 3)  # 213
print get_permutation(4, 9)  # 2314
