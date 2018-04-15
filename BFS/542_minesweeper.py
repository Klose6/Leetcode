"""
Minesweeper 542
https://discuss.leetcode.com/topic/80917/10-line-python-solution
https://discuss.leetcode.com/topic/80802/java-solution-dfs-bfs
"""

def updateBoard(board, click):
  if not board or not click:
    return None
  m, n = len(board), len(board[0])
  dirs = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
  row, col = click
  if 0<=row<m and 0<=col<n:
    if board[row][col] == 'M':
      board[row][col] = 'X'
    elif board[row][col] == "E":
      count = sum([board[row+i][col+j]=="M" for i,j in dirs if 0<=row+i<m and 0<=col+j<n])
      if count == 0:
        board[row][col] = "B"
        for dir in dirs:
          updateBoard(board, [row+dir[0], col+dir[1]])
      else:
        board[row][col] = str(count)

def updateBoard_1(board, click):
  (row, col), directions = click, ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
  if 0 <= row < len(board) and 0 <= col < len(board[0]):
    if board[row][col] == 'M':
      board[row][col] = 'X'
    elif board[row][col] == 'E':
      n = sum([board[row + r][col + c] == 'M' for r, c in directions if
               0 <= row + r < len(board) and 0 <= col + c < len(board[0])])
      board[row][col] = str(n or 'B')
      for r, c in directions * (not n): updateBoard(board, [row + r, col + c])
  return board

board = [list("EEEEE"), list("EEMEE"), list("EEEEE"), list("EEEEE")]
click = [3,0]
updateBoard(board, click)
print(board)
