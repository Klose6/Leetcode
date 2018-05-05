"""
set matrix zeros
"""


def set_matrix_zeros(matrix):
	if not matrix:
		return matrix
	m, n = len(matrix), len(matrix[0])
	col0 = False
	for i in range(m):
		if not matrix[i][0]:
			col0 = True
		for j in range(1, n):
			if not matrix[i][j]:
				matrix[i][0] = matrix[0][j] = 0
	for i in range(m)[::-1]:
		for j in range(1, n)[::-1]:
			if matrix[i][0] == 0 or matrix[0][j] == 0:
				matrix[i][j] = 0
		if col0:
			matrix[i][0] = 0
	return matrix


m2 = [[0, 1, 2, 0],
			[3, 4, 5, 2],
			[1, 3, 1, 5]]
print set_matrix_zeros(m2)
