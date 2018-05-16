""""
87 scramble string
"""
from collections import Counter


def can_scramble(s1, s2):
	if s1 == s2:
		return True
	if len(s1) != len(s2):
		return False
	if Counter(s1) != Counter(s2):
		return False
	n = len(s1)
	for i in range(1, n):
		if can_scramble(s1[:i], s2[:i]) and can_scramble(s1[i:], s2[i:]):
			return True
		if can_scramble(s1[:i], s2[n - i:]) and can_scramble(s1[n - i:], s2[:i]):
			return True
	return False


print can_scramble("great", "rgeat")  # True
print can_scramble("abcde", "caebd")  # False
