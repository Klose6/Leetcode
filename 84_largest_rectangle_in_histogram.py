"""
84 largest rectangle in histogram
"""


def largest_rectangle(heights):
	res = 0
	stack = [-1]
	heights.append(0)
	for i in range(len(heights)):
		while heights[i] < heights[stack[-1]]:
			h = heights[stack.pop()]
			w = i - stack[-1] - 1
			res = max(res, h * w)
		stack.append(i)
	heights.pop()
	return res


print largest_rectangle([2, 1, 5, 6, 2, 3])  # 10
