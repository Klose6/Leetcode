"""
38 count and say
"""
import re
import itertools


def count_and_say(n):
	s = "1"
	for _ in range(n - 1):
		s = ".".join(str(len(list(group))) + digit
								 for digit, group in itertools.groupby(s))
	return s


def count_and_say2(n):
	s = "1"
	for i in range(n - 1):
		s = re.sub(r"(.)\1*", lambda m: str(len(m.group(0))) + m.group(1), s)
	return s


print count_and_say(2)  # 21
print count_and_say2(2)
