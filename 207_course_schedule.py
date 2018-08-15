"""
207 course schedule
https://leetcode.com/problems/course-schedule/discuss/58509/18-22-lines-C++-BFSDFS-Solutions
"""


def can_finish(num_courses, prerequisites):
	# using topological sort
	matrix = [[0] * num_courses for _ in range(num_courses)]
	indegrees = [0] * num_courses
	for pre in prerequisites:
		if matrix[pre[1]][pre[0]] == 0:
			indegrees[pre[0]] += 1  # duplicate case
		matrix[pre[1]][pre[0]] = 1
	q, count = [], 0
	for i, v in enumerate(indegrees):
		if v == 0:
			q.append(i)
	while q:
		count += 1
		course = q.pop(0)
		for i in range(num_courses):
			if matrix[course][i]:
				indegrees[i] -= 1
				if indegrees[i] == 0:
					q.append(i)
	return count == num_courses


print can_finish(2, [[1, 0]]) == True
