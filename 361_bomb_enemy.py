"""
361 Bomb Enemy
http://www.cnblogs.com/grandyang/p/5599289.html
"""
class Solution(object):
	def max_killed_enemies_1(self, grid):
		r, c = len(grid), len(grid[0])
		colcount = [0]*c
		colhits = 0
		res = 0
		for i in range(r):
			for j in range(c):
				if not j or grid[i][j]=="W":
					colhits = 0
					k = j
					while k < c and grid[i][k] != "W":
						if grid[i][k] == "E":
							colhits += 1
						k += 1
				if not i or grid[i-1][j] == "W":
					colcount[j] = 0
					k = i
					while k < r and grid[k][j] != "W":
						if grid[k][j] == "E":
							colcount[j] += 1
						k += 1
				if grid[i][j] == "0":
					res = max(res, colcount[j]+colhits)
		return res

	def max_killed_enemies_2(self, grid):
		if not grid:
			return 0
		r, c = len(grid), len(grid[0])
		lr = [[0]*c for _ in range(r)]
		rl = [[0]*c for _ in range(r)]
		td = [[0]*c for _ in range(r)]
		dt = [[0]*c for _ in range(r)]
		for i in range(r):
			for j in range(c):
				if grid[i][j] == "E":
					lr[i][j] = lr[i][j-1]+1 if j>0 else 1
				elif grid[i][j] == "W":
					lr[i][j] = 0
				elif j>0:
					lr[i][j] = lr[i][j-1]
		for i in range(r):
			for j in range(c)[::-1]:
				if grid[i][j] == "E":
					rl[i][j] = rl[i][j+1]+1 if j<c-1 else 1
				elif grid[i][j] == "W":
					rl[i][j] = 0
				elif j<c-1:
					rl[i][j] = rl[i][j+1]
		for j in range(c):
			for i in range(r):
				if grid[i][j] == "E":
					td[i][j] = td[i-1][j]+1 if i>0 else 1
				elif grid[i][j] == "W":
					td[i][j] = 0
				elif i>0:
					td[i][j] = td[i-1][j]
		for j in range(c):
			for i in range(r)[::-1]:
				if grid[i][j] == "E":
					dt[i][j] = dt[i+1][j]+1 if i<r-1 else 1
				elif grid[i][j] == "W":
					dt[i][j] = 0
				elif i<r-1:
					dt[i][j] = dt[i+1][j]
		res = 0
		for i in range(r):
			for j in range(c):
				if grid[i][j] == "0":
					res = max(res, lr[i][j]+rl[i][j]+td[i][j]+dt[i][j])
		return res

s = Solution()
print s.max_killed_enemies_1([list("0E00"),list("E0WE"),list("0E00")])#3
print s.max_killed_enemies_2([list("0E00"),list("E0WE"),list("0E00")])#3