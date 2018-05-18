"""
93 restore ip addresses
"""


def is_valid(s):
	if not s or len(s) > 3 or (s[0] == "0" and len(s) > 1) or int(s) > 255:
		return False
	return True


def restore_ip(s):
	res = []
	n = len(s)
	for i in range(1, min(4, n - 2)):
		for j in range(i + 1, min(i + 4, n - 1)):
			for k in range(j + 1, min(j + 4, n)):
				if is_valid(s[:i]) and is_valid(s[i:j]) and \
						is_valid(s[j:k]) and is_valid(s[j:]):
					res.append(s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:])
	return res


print restore_ip("11223")
