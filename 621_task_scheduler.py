"""
task scheduler
https://leetcode.com/problems/task-scheduler/description/
https://discuss.leetcode.com/topic/92852/concise-java-solution-o-n-time-o-26-space
https://discuss.leetcode.com/topic/92952/python-straightforward-with-explanation
"""

from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        if not tasks or n <0: raise ValueError
        counts = list(Counter(tasks).values())
        m = max(counts)
        times = counts.count(m)
        return max(len(tasks), (m-1)*(n+1) + times)
