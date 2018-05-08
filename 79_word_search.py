"""
79 word search
"""


def word_search(board, word):
	if not board or not word:
		return False
	for i, r in enumerate(board):
		for j, c in enumerate(r):
			if exist(board, i, j, word, 0):
				return True
	return False


def exist(board, i, j, word, idx):
	if idx == len(word):
		return True
	if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or \
					board[i][j] != word[idx]:
		return False
	# board[i][j] ^= 256
	tmp = board[i][j]
	board[i][j] = "#"
	find = exist(board, i - 1, j, word, idx + 1) or \
				 exist(board, i + 1, j, word, idx + 1) or \
				 exist(board, i, j - 1, word, idx + 1) or \
				 exist(board, i, j + 1, word, idx + 1)
	# board[i][j] ^= 256
	board[i][j] = tmp
	return find


board = [
	['A', 'B', 'C', 'E'],
	['S', 'F', 'C', 'S'],
	['A', 'D', 'E', 'E']
]

print word_search(board, "ABCCED")  # true
print word_search(board, "SEE")  # true
print word_search(board, "ABCB")  # false
