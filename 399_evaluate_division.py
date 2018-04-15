"""
399 evaluate division
using graph
"""
from collections import defaultdict

class Solution(object):
	def evaluate(self, equations, values, queries):
		if not queries or not equations or not values:
			return -1.0
		pairs = defaultdict(list)
		pairvalues = defaultdict(list)
		for i in range(len(equations)):
			pairs[equations[i][0]].append(equations[i][1])
			pairs[equations[i][1]].append(equations[i][0])
			pairvalues[equations[i][0]].append(values[i])
			pairvalues[equations[i][1]].append(1.0/values[i])
		res = []
		for i, j in queries:
			res.append(self.dfs(i, j, pairs, pairvalues, set(), 1.0))
		return res
	def dfs(self,i,j,pairs,values,visited,preval):
		if i not in pairs:
			return -1.0
		if i == j:
			return preval
		for p, v in zip(pairs.get(i), values.get(i)):
			if p not in visited:
				visited.add(p)
				curres = self.dfs(p, j, pairs, values, visited, preval*v)
				if curres != -1.0:
					return curres
				visited.remove(p)
		return -1.0
s=Solution()
equations=[["a", "b"], ["b", "c"]]
values=[2.0, 3.0]
print s.evaluate(equations, values, [["a", "c"], ["c", "b"]])
