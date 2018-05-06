"""
74 search 2D matrix
"""


def search_2d_matrix(matrix, target):
	if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:
		return -1, -1
	m, n = len(matrix), len(matrix[0])
	lo, hi = 0, m * n - 1
	while lo <= hi:
		mid = lo + (hi - lo) / 2
		i, j = mid / n, mid % n
		if matrix[i][j] == target:
			return i, j
		elif matrix[i][j] > target:
			hi = mid - 1
		else:
			lo = mid + 1
	return -1, -1


matrix = [
	[1, 3, 5, 7],
	[10, 11, 16, 20],
	[23, 30, 34, 50]
]
target = 3
print search_2d_matrix(matrix, target)
