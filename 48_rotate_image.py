"""
48 rotate image
"""


def rotate_image(matrix):
	if not matrix:
		return
	# m[i][j]->m[j][n-i]->m[n-i][n-j]->m[n-j][i]
	n = len(matrix)
	for i in range(n - 1):
		for j in range(i, n - i - 1):
			first = matrix[i][j]
			second = matrix[j][n - 1 - i]
			third = matrix[n - 1 - i][n - 1 - j]
			forth = matrix[n - 1 - j][i]
			matrix[j][n - 1 - i] = first
			matrix[n - 1 - i][n - 1 - j] = second
			matrix[n - 1 - j][i] = third
			matrix[i][j] = forth
	return matrix


print rotate_image([[1, 2], [3, 4]])
