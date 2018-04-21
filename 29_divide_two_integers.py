"""
29 divide two integers
"""


def divide_two_integers(dividend, divisor):
	if divisor == 0:
		raise ValueError
	sign = dividend < 0 is divisor < 0
	dividend, divisor = abs(dividend), abs(divisor)
	res = 0
	while dividend >= divisor:
		tmp, i = divisor, 1
		while dividend >= tmp:
			dividend -= tmp
			res += i
			tmp <<= 1
			i <<= 1
	if not sign:
		res = -res
	return min(2 ** 31 - 1, max(res, -2 ** 31))


print divide_two_integers(7, -3)
