"""
44 wildcard matching
"""


def wildcard_matching(s, p):
	sidx, pidx, match, start_idx = 0, 0, 0, -1
	m, n = len(s), len(p)
	while sidx < m:
		if pidx < n and (p[pidx] == "?" or s[sidx] == p[pidx]):
			pidx += 1
			sidx += 1
		# find *, only advance pattern idx
		elif pidx < n and p[pidx] == "*":
			start_idx = pidx
			match = sidx
			pidx += 1
		# last pattern idx was *, advance the string idx
		elif start_idx != -1:
			pidx = start_idx + 1
			match += 1
			sidx = match
		else:
			return False
	# check for remaining letters in pattern
	while pidx < n and p[pidx] == "*":
		pidx += 1
	return pidx == n


def wildcard_matching2(s, p):
	m, n = len(s), len(p)
	match = [[False] * (n + 1) for _ in range(m + 1)]
	match[m][n] = True
	for i in reversed(range(n)):
		if p[i] != "*":
			break
		match[m][i] = True
	for i in reversed(range(m)):
		for j in reversed(range(n)):
			if s[i] == p[j] or p[j] == "?":
				match[i][j] = match[i + 1][j + 1]
			elif p[j] == "*":
				match[i][j] = match[i + 1][j] or match[i][j + 1]
	# print match
	return match[0][0]


print wildcard_matching("aa", "a")
print wildcard_matching("cb", "?*")
print wildcard_matching2("aa", "a")
print wildcard_matching2("cb", "?*")
