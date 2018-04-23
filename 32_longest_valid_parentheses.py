"""
32 longest valid parentheses
"""


def longest_valid_parentheses(s):
	# O(n)
	if not s or len(s) < 2:
		return 0
	n = len(s)
	longest = [0] * n
	max_len = 0
	for i in range(1, n):
		if s[i] == ")" and i - longest[i - 1] - 1 >= 0 and s[i - longest[i - 1] - 1] == "(":
			longest[i] = longest[i - 1] + 2 + longest[i - longest[i - 1] - 2] if i - longest[i - 1] - 2 >= 0 else 0
			max_len = max(max_len, longest[i])
	return max_len


print longest_valid_parentheses("(()")  # 2
print longest_valid_parentheses(")()())")  # 4
