
def diagonal_traverse(matrix):
  if matrix is None:
    return
  m = len(matrix)
  n = len(matrix[0])
  dirs = ((-1, 1), (1, -1))
  col, row, d = 0, 0, 0
  for i in range(m*n):
    print(matrix[row][col])
    row += dirs[d][0]
    col += dirs[d][1]
    if row >= m:
      row -= 1
      col += 2
      d = 1-d
    if col >= n:
      row += 2
      col -= 1
      d = 1-d
    if row < 0:
      row = 0
      d = 1-d
    if col < 0:
      col = 0
      d = 1-d

#https://discuss.leetcode.com/topic/77933/sorting-and-normal-python
def diagonalTraverse2(matrix):
  if matrix is None:
    return
  entries = [(i+j, (j, i)[(i^j)&1], val) for i,row in enumerate(matrix)
             for j,val in enumerate(row)]
  return [e[2] for e in sorted(entries)]

def diagonalTraverse3(matrix):
  if matrix is None:
    return
  m,n = len(matrix), len( matrix[0])
  return [matrix[i][d-i]
            for d in range(m+n-1)
            for i in range(max(0, d-n+1), min(m, d+1))[::d%2*2-1]]
matrix = [[1,2,3], [4,5,6], [7,8,9]]
#diagonal_traverse(matrix)

#traverse = [val for i,row in enumerate(matrix) for j,val in enumerate(row)]
#print(traverse)

print(diagonalTraverse2(matrix))
print(diagonalTraverse3(matrix))