"""
289 game of life
"""
class Solution(object):
	def gameoflife(self, board):
		if not board:
			return board
		m, n=len(board), len(board[0])
		for i in xrange(m):
			for j in xrange(n):
				nn = self.get_neighbors(board, i, j )
				if board[i][j] and (nn==2 or nn==3):
					board[i][j] |= 2
				if not board[i][j] and nn==3:
					board[i][j] |= 2
		for i in xrange(m):
			for j in xrange(n):
				board[i][j] >>=1
	def get_neighbors(self, board, i, j):
		m, n=len(board), len(board[0])
		count = 0
		if i-1>=0 and i-1>=0:
			count += board[i-1][j-1]%2
		if i-1 >=0:
			count+=board[i-1][j]%2
		if i-1>=0 and j+1<=n:
			count+=board[i-1][j+1]%2
		if j-1>0:
			count += board[i][j-1]%2
		if j+1<n:
			count+=board[i][j+1]%2
		if i+1<m and j-1>=0:
			count+=board[i+1][j-1]%2
		if i+1<m:
			count+=board[i+1][j]%2
		if i+1<m and j+1<n:
			count+=board[i+1][j+1]%2
		return count
