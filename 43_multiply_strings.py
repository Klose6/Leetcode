"""
43 multiply strings
"""


def multiple(num1, num2):
	if not num1 or not num2:
		raise ValueError("Value Error")
	m, n = len(num1), len(num2)
	res = [0] * (m + n)
	for i in range(m):
		for j in range(n):
			res[i + j + 1] += int(num1[i]) * int(num2[j])
	carry = 0
	for k in range(len(res))[::-1]:
		res[k] += carry
		carry = res[k] / 10
		res[k] %= 10
	return "".join([str(i) for i in res]).lstrip("0")


print multiple("2", "3")
print multiple("123", "456")
