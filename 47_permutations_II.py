"""
47 permutations II
"""


def permutations2(nums):
	if not nums:
		return []
	res = [[]]
	for n in nums:
		new_p = []
		for l in res:
			for i in range(len(l) + 1):
				new_p.append(l[:i] + [n] + l[i:])
				# avoid inserting a number before any of its duplicates
				if i < len(l) and l[i] == n:
					break
		res = new_p
	return res


print permutations2([1, 2, 1])
print permutations2([1, 1])
