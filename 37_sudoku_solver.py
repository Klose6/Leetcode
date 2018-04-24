"""
37 sudoku solver
"""


def sudoku_solver(board):
	if not board:
		return solve(board)


def solve(board):
	for i, r in enumerate(board):
		for j, c in enumerate(r):
			if c == ".":
				for k in range(1, 10):
					if is_valid(board, i, j, str(k)):
						board[i][j] = str(k)
						if solve(board):
							return True
						else:
							board[i][j] = "."
	return False


def is_valid(board, i, j, c):
	for k in range(1, 10):
		if board[i][k] != "." and board[i][k] == c: return False
		if board[k][j] != "." and board[k][j] == c: return False
		if board[i / 3 * 3 + k / 3][j / 3 * 3 + k % 3] != "." and board[i / 3 * 3 + k / 3][
									j / 3 * 3 + k % 3] == c: return False
	return True
