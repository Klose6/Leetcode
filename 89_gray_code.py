"""
89 Gray code
"""


def gray_code(n):
	res = []
	for i in range(1 << n):
		res.append(i ^ i >> 1)
	return res


print gray_code(3)
