"""
200 num of islands
"""


def num_of_islands(grid):
	count = 0
	for i, c in enumerate(grid):
		for j, r in enumerate(c):
			if grid[i][j] == '1':
				count += 1
				dfs(grid, i, j)
	# can chane the # back to 1 as needed
	print grid
	return count


def dfs(grid, i, j):
	m, n = len(grid), len(grid[0])
	if not 0 <= i < m or not 0 <= j < n or grid[i][j] != '1':
		return
	grid[i][j] = '#'
	for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
		dfs(grid, i + d[0], j + d[1])


grid = [list("11000"), list("11000"), list("00100"),
				list("00011")]
print num_of_islands(grid) == 3
