"""
36 valid sudoku
"""
from collections import Counter


def valid_sudoku(board):
	# +[1] for empty board
	return 1 == max(Counter([
		x for i, r in enumerate(board)
		for j, c in enumerate(r)
		if c != "."  # c is str
		for x in ((c, i), (j, c), (i / 3, j / 3, c))]).values() + [1])
