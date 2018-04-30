"""
51 N queens
"""


def solve_n_queens(n):
	res = []

	def dfs(queens, xy_diff, xy_sum):
		p = len(queens)
		if p == n:
			res.append(queens)
			return
		for q in range(n):
			if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
				dfs(queens + [q], xy_diff + [p - q], xy_sum + [p + q])

	dfs([], [], [])
	return [["." * x + "Q" + "." * (n - 1 - x) for x in sol] for sol in res]
