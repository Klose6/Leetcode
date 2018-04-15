"""
cut off trees for golf event
"""
from heapq import heappush, heappop
from collections import deque

class Solution(object):
	def cut_trees(self, forest):
		if not forest:
			return -1
		trees = []
		m,n = len(forest), len(forest[0])
		for i in range(m):
			for j in range(n):
				if forest[i][j]>1:
					trees.append((forest[i][j], i, j))
		trees=sorted(trees)
		cur = (0,0)
		res=0
		for h,x,y in trees:
			steps = self.findnext(forest, cur, (x,y))
			if steps == -1:
				return -1
			res += steps
			cur = (x,y)
		return res
	def findnext(self, forest, cur, target):
		# BFS
		m, n=len(forest), len(forest[0])
		q = deque()
		q.append(cur)
		step = 0
		visited = [[False]*n for _ in range(m)]
		visited[cur[0]][cur[1]] = True
		while q:
			size = len(q)
			for i in xrange(size):
				next = q.popleft()
				if next == target:
					return step
				x, y = next
				for nx,ny in [(x-1, y),(x+1,y),(x,y-1),(x,y+1)]:
					if nx <0 or nx >= m or ny<0 or ny>=n or visited[nx][ny] or \
							forest[nx][ny] ==0:
						continue
					visited[nx][ny] = True
					q.append((nx, ny))
			step += 1
		return -1

s=Solution()
forest = [[1,2,3],[0,0,4],[7,6,5]]
print s.cut_trees(forest) #6
forest=[[1,2,3],[0,0,0],[7,6,5]]
print s.cut_trees(forest) #-1