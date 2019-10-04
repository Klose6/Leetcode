"""
minimum window substring
"""

from collections import Counter, defaultdict


def minWindow(s: str, t: str) -> str:
	if not s or not t or len(s) < len(t): return ""
	required = Counter(t)
	requiredCounter = len(required)
	formed = 0
	window = defaultdict(int)
	res = (float("inf"), 0, 0)
	l = 0
	for i, c in enumerate(s):
		window[c] += 1
		if window[c] == required[c]:
			formed += 1
		while l <= i and formed == requiredCounter:
			if i - l + 1 < res[0]:
				res = (i - l + 1, l, i)
			window[s[l]] -= 1
			if s[l] in required and window[s[l]] < required[s[l]]:
				formed -= 1
			l += 1
	return "" if res[0] == float("inf") else s[res[1]: res[2] + 1]

def min_window_substring(s, t):
	if not s or len(s) < len(t):
		return
	need, missing = Counter(t), len(t)
	i, start, end = 0, 0, 0
	for j, c in enumerate(s, 1):
		missing -= need[c] > 0
		need[c] -= 1
		if not missing:
			while i < j and need[s[i]] < 0:
				need[s[i]] += 1
				i += 1
			if not end or j - i <= end - start:
				start, end = i, j
	return s[start:end]


print(min_window_substring("ADOBECODEBANC", "ABC"))  # BANC
print(min_window_substring("a", "b")) # ""
print(min_window_substring("a", "a")) # a"
