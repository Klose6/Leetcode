"""
77 combinations
"""
import itertools


def combine(n, k):
	return list(itertools.combinations(range(1, n + 1), k))


def combine2(n, k):
	if k == 0:
		return [[]]
	return [pre + [i] for i in range(k, n + 1)
					for pre in combine2(i - 1, k - 1)]


def combine3(n, k):
	res = [[]]
	for _ in range(k):
		res = [[i] + c for c in res for i in range(1, c[0] if c else n + 1)]
	return res


print combine(3, 2)
print combine2(3, 2)
print combine3(3, 2)
