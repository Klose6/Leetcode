"""
851 loud and rich
For every people, call a sub function dfs to compare the quiet with others, who is richer than him.
Also we will note this answer to avoid repeated calculation.
"""
import collections


class Solution(object):
	def loud_and_rich(self, richer, quiet):
		map = collections.defaultdict(list)
		for i, j in richer:
			map[j].append(i)
		n = len(quiet)
		res = [-1] * n

		def dfs(i):
			if res[i] >= 0: return res[i]
			for j in map[i]:
				if quiet[res[i]] > quiet[dfs(j)]:
					res[i] = res[j]
			return res[i]

		for i in range(n):
			dfs(i)
		return res
