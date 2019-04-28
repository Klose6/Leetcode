"""
529 minesweeper
"""

def minesweeper(board, click):
  dirs = ((-1, -1), (0, -1), (-1, 0), (1, 0), (0, 1), (1, 1), (-1, 1), (1, -1))
  row, col = click # make the variables shorter
  m, n = len(board), len(board[0])
  if 0 <= row < m and 0 <= col < n:
    if board[row][col] == "M":
      board[row][col] = "X"
      return
    if board[row][col] == "E":
      num_mines = 0
      for i, j in dirs:
        p, q = i + row, j + col
        if 0 <= p < m and 0 <= q < n and board[p][q] == "M":
          num_mines += 1
      if num_mines == 0:
        board[row][col] = "B"
        for i, j in dirs: # set the board recursively
          minesweeper(board, [row + i, col + j])
      else:
        board[row][col] = str(num_mines)
  return board

board = [ list("EEEEE"), list("EEMEE"), list("EEEEE"), list("EEEEE")]
print(minesweeper(board, [3, 0]))
