"""
84 largest rectangle in histogram
"""


def largest_rectangle(heights):
	res = 0
	stack = []
	n = len(heights)
	i = 0
	while i <= n:
		bar = heights[i] if i < n else 0
		if not stack or bar >= heights[stack[-1]]:
			stack.append(i)
			i += 1
		else:
			height = heights[stack.pop()]
			while stack and height == heights[stack[-1]]:
				stack.pop()
			left = 0 if not stack else stack[-1] + 1
			res = max(res, height * (i - left))
	return res


print largest_rectangle([2, 1, 5, 6, 2, 3])  # 10
