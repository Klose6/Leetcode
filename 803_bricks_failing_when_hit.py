"""
803 bricks falling when hit
"""

class Solution(object):
	def hit_bricks(self, grid, hits):
		self.remove_hit_bricks(grid, hits)
		self.mark_remain_bricks(grid)
		return self.search_falling_bricks(grid, hits)

	def remove_hit_bricks(self, grid, hits):
		for i,j in hits:
			grid[i][j] -= 1

	def mark_remain_bricks(self, grid):
		"""Mark whether there is a brick at each hit """
		for i in range(0, len(grid[0])):
			self.dfs(grid, 0, i)

	def dfs(self, grid, i, j):
		"""Get grid after all hits"""
		m, n = len(grid), len(grid[0])
		if not (0<=i<m and 0<=j<n) or grid[i][j] != 1:
			return 0
		res = 1
		grid[i][j] = 2
		res += sum(self.dfs(grid,x,y) for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)))
		return res

	def search_falling_bricks(self, grid, hits):
		"""Reverse the problem and count how many new no-dropping bricks are added when
		adding the bricks reversely"""
		result = [0] * len(hits)
		for k in range(len(hits))[::-1]:
			i, j = hits[k]
			grid[i][j] += 1
			if grid[i][j] == 1 and self.is_connect_to_top(grid, i, j):
					result[k] = self.dfs(grid, i, j)-1
		return result

	def is_connect_to_top(self, grid, i, j):
		m, n = len(grid), len(grid[0])
		return i==0 or any([0<=x<m and 0<=y<n and grid[x][y]==2 for x,y in
												((i-1,j),(i+1,j),(i,j-1),(i,j+1))])

s=Solution()
grid = [[1,0,0,0], [1,1,1,0]]
hits = [[1,0]]
print s.hit_bricks(grid, hits) #[2]
grid = [[1,0,0,0], [1,1,0,0]]
hits = [[1,1],[1,0]]
print s.hit_bricks(grid, hits) #[0,0]
