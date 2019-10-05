
"""
253 meeting room II
"""
from heapq import heappush, heapreplace

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        intervals.sort(key=lambda i: i[0])
        h = [intervals[0][1]]
        for i in intervals[1:]:
            if h and i[0] >= h[0]:
                heapreplace(h, i[1])
            else:
                heappush(h, i[1])
        return len(h)