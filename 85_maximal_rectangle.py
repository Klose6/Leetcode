"""
85 maximal rectangle
"""


def max_rectangle(matrix):
	if not matrix:
		return 0
	m, n = len(matrix), len(matrix[0])
	height = [0] * n
	left, right = [0] * n, [n] * n
	res = 0
	for i in range(m):
		cur_left, cur_right = 0, n
		for j in range(n):
			if matrix[i][j] == '1':
				height[j] += 1
			else:
				height[j] = 0
		for j in range(n):
			if matrix[i][j] == '1':
				left[j] = max(left[j], cur_left)
			else:
				left[j] = 0
				cur_left = j + 1
		for j in range(n)[::-1]:
			if matrix[i][j] == '1':
				right[j] = min(right[j], cur_right)
			else:
				right[j] = n
				cur_right = j
		for j in range(n):
			res = max(res, (right[j] - left[j]) * height[j])
	return res


matrix = [["1", "0", "1", "0", "0"],
					["1", "0", "1", "1", "1"],
					["1", "1", "1", "1", "1"],
					["1", "0", "0", "1", "0"]]
print max_rectangle(matrix)  # 6
