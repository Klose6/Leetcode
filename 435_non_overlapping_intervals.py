"""
435 non-overlapping intervals
https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python
"""

def eraseOverlapIntervals(intervals):
  """
  Keep the intervals with the smallest end and remove the other overlapped ones
  """
  if not intervals or len(intervals) < 2:
    return 0
  end = float("-inf")
  count = 0
  for i in sorted(intervals, key=lambda x: x[1]):
    if i[0] >= end:
      end = i[1]
    else:
      count += 1
  return count

print(eraseOverlapIntervals([[1,2], [2,3], [3,4], [1,3]])) #1
