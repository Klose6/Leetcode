"""
49 group anagrams
"""

from collections import defaultdict


def group_anagams(strs):
	if not strs:
		return
	groups = defaultdict(list)
	for str in strs:
		# list is not hashable
		groups[tuple(sorted(str))].append(str)
	return map(sorted, groups.values())


print group_anagams(["eat", "tea", "tan", "ate", "nat", "bat"])
