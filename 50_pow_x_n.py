"""
50 pow(x, n)
"""


def pow(x, n):
	if not n:
		return 1
	if n < 0:
		return 1.0 / pow(x, -n)
	return pow(x * x, n / 2) if n % 2 == 0 else x * pow(x * x, n / 2)


def pow2(x, n):
	if not n:
		return 1
	if n < 0:
		n = -1
		x = 1.0 / x
	res = 1.0
	while n > 0:
		if n & 1:
			res *= x
		x *= x
		n >>= 1
	return res


print pow(2, 4)
print pow2(2, 5)
