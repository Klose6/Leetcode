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


from collections import Counter
from heapq import heappop, heappush, heapify

class Solution1:
    def leastInterval(self, tasks, n):
        if not tasks or n < 0: raise ValueError
        q = [(-v, k) for k,v in Counter(tasks).items()]
        print(f"q: {q}")
        count = 0
        k = n+1
        while q:
            tmp = [heappop(q) for i in range(k) if q]
            print(f"{tmp}")
            if not tmp: break
            # for the last round, no need to add n+1
            count = count+k if tmp[0][0] < -1 else count + len(tmp)
            for t, c in tmp:
                t += 1
                if t < 0:
                    heappush(q, (t, c))
        return count

print(Solution1().leastInterval(["A","A","A","B","B","B"], 2))