"""
54 spiral matrix
"""


def spiral_matrix(matrix):
	if not matrix:
		return
	top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
	res = []
	while top <= bottom and left <= right:
		# traverse from left to right
		for i in range(left, right + 1):
			res.append(matrix[top][i])
		top += 1
		# traverse from top to bottom
		for i in range(top, bottom + 1):
			res.append(matrix[i][right])
		right -= 1
		# traverse from right ot left
		if left <= right:
			for i in range(right, left - 1, -1):
				res.append(matrix[bottom][i])
			bottom -= 1
		# traverse from bottom to top
		if top >= bottom:
			for i in range(bottom, top - 1, -1):
				res.append(matrix[i][left])
			left += 1
	return res


print spiral_matrix([[1, 2], [3, 4]])
print spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
