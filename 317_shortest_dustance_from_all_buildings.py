"""
317 shortest distance from all buildings
"""
import copy

class Solution(object):
	def get_shortest_distance(self, grid):
		if not grid:
			return
		m, n= len(grid), len(grid[0])
		total = [[0]*n for _ in range(m)]
		walk = 0
		dirs = (0, 1, 0, -1, 0)
		minres=-1
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					#bfs
					dis = copy.deepcopy(grid)
					q = [(i,j)]
					minres=-1
					while len(q):
						x, y = q.pop(0)
						for k in range(4):
							xx, yy = x+dirs[k], y+dirs[k+1]
							if xx>=0 and xx<m and yy>=0 and yy<n and grid[xx][yy]==walk:
								grid[xx][yy]-=1
								dis[xx][yy] = dis[x][y] + 1
								total[xx][yy] += dis[xx][yy]-1
								q.append((xx, yy))
								if minres<0 or total[xx][yy] < minres:
									minres=total[xx][yy]
					walk-=1
		return minres
s=Solution()
print s.get_shortest_distance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]) #7