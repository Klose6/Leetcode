"""
351 android unlock patterns
1 2 3
4 5 6
7 8 9
"""

class Solution(object):
	def unlock_patterns(self, m, n):
		vis = [False]*10
		# skip array represent the number to skip between two numbers
		skip = [[0]*10 for _ in range(10)]
		skip[1][3]=skip[3][1]=2
		skip[1][7]=skip[7][1]=4
		skip[1][9]=skip[9][1]=5
		skip[2][8]=skip[8][2]=5
		skip[3][7]=skip[7][3]=5
		skip[3][9]=skip[9][3]=6
		skip[4][6]=skip[6][4]=5
		res=0
		for i in range(m, n+1):
			res += 4*self.dfs(vis, skip, 1, i-1)
			res += 4*self.dfs(vis, skip, 2, i-1)
			res += self.dfs(vis, skip, 5, i-1)
		return res
	def dfs(self, vis, skip, cur, remain):
		if remain < 0:
			return 0
		if remain == 0:
			return 1
		vis[cur] = True
		res = 0
		for i in range(1, 10):
			if not vis[i] and (not skip[cur][i] or vis[skip[cur][i]]):
				res += self.dfs(vis, skip, i, remain-1)
		vis[cur] = False
		return res
s=Solution()
print s.unlock_patterns(1, 1) #9
