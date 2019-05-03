
def diagonal_traverse(matrix):
  if matrix is None:
    return
  m, n = len(matrix), len(matrix[0])
  dirs = ((-1, 1), (1, -1)) # there is only 2 directions
  col, row, d = 0, 0, 0 # the start point and direction
  res = []
  for i in range(m*n): # for all the elements
    res.append(matrix[row][col])
    row += dirs[d][0]
    col += dirs[d][1]
    # very time meet a boundary, need to change the direction
    if row >= m: # for the bottom boundary
      row -= 1
      col += 2
      d = 1-d
    if col >= n: # for the right boundary
      row += 2
      col -= 1
      d = 1-d
    if row < 0: # for the top boundary
      row = 0
      d = 1-d
    if col < 0: # for the left boundary
      col = 0
      d = 1-d
  return res

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
  m,n = len(matrix), len(matrix[0])
  return [matrix[i][d-i]
            for d in range(m+n-1)
            for i in range(max(0, d-n+1), min(m, d+1))[::d%2*2-1]]
matrix = [[1,2,3], [4,5,6], [7,8,9]]
#diagonal_traverse(matrix)

#traverse = [val for i,row in enumerate(matrix) for j,val in enumerate(row)]
#print(traverse)

print(diagonalTraverse2(matrix))
print(diagonalTraverse3(matrix))