"""
207 course schedule
"""


def can_finish(num_courses, prerequisites):
	# using topological sort
	matrix = [[0] * num_courses for _ in range(num_courses)]
	indegrees = [0] * num_courses
	for pre in prerequisites:
		if matrix[pre[0]][pre[1]] == 0:
			indegrees[pre[0]] += 1  # duplicate case
		matrix[pre[0]][pre[1]] = 1
	q, count = [], 0
	for i, v in enumerate(indegrees):
		if v == 0:
			q.append(i)
	while q:
		count += 1
		course = q.pop()
		for i in range(num_courses):
			if matrix[course][i]:
				indegrees[course][i] -= 1
				if indegrees == 0:
					q.append(i)
	return count == num_courses
