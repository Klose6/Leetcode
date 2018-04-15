"""
task scheduler
https://leetcode.com/problems/task-scheduler/description/
https://discuss.leetcode.com/topic/92852/concise-java-solution-o-n-time-o-26-space
https://discuss.leetcode.com/topic/92952/python-straightforward-with-explanation
"""

def least_intervals(tasks, n):
	if not tasks:
		return 0
