"""
20 valid parentheses
"""


def is_valid(s):
	stack = []
	M = {"]": "[", "}": "{", ")": "("}
	for c in s:
		if c in M.values():
			stack.append(c)
		elif c in M:
			if not stack or stack.pop() != M[c]:
				return False
		else:
			return False
	return stack == []


print is_valid("[]")
print is_valid("[{}]")
print is_valid("([})")
