"""
363 max sum of rectangles no larger than K
"""


def maxSumSubmatrix(matrix, k):
  """
  :type matrix: List[List[int]]
  :type k: int
  :rtype: int
  """
  if not matrix:  return 0

  res = float('-inf')
  rows, columns = len(matrix), len(matrix[0])
  for i in range(columns):
    sums = [0 for _ in range(rows)]
    for j in range(i, columns):
      for r in range(rows):
        sums[r] += matrix[r][j]

      # find the largest sum of a subarray which is no more than K
      import bisect
      cum_sum = [0]
      cum, max_sum = 0, float('-inf')
      for item in sums:
        cum += item
        left = bisect.bisect_left(cum_sum, cum - k)
        print(f"***{cum_sum} , {cum - k}, {left}")
        if left < len(cum_sum):
          max_sum = max(max_sum, cum - cum_sum[left])
        bisect.insort(cum_sum, cum)
      res = max(res, max_sum)
  return res

from bisect import bisect_left, insort

def maxSumSubmatrix1(matrix, k):
  if not matrix: return 0
  res = float("-inf")
  m, n = len(matrix), len(matrix[0])
  # using the Kadane's algorithm
  for i in range(n):
    sums = [0] * m
    for j in range(i, n):
      for r in range(m):
        sums[r] += matrix[r][j]
      # print(f"sums: {sums}")
      accuSums = [0]
      curSum, curMax = 0, float("-inf")
      for s in sums:
        curSum += s
        idx = bisect_left(accuSums, curSum - k)
        print(f"{accuSums} , {curSum-k}, {idx}")
        if idx < len(accuSums):
          curMax = max(curMax, curSum-accuSums[idx])
        insort(accuSums, curSum)
      res = max(res, curMax)
  return res
print(maxSumSubmatrix1([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], -1))
# print(maxSumSubmatrix([[1,0,1], [0,-2,3]], 2)) # 2
# print(maxSumSubmatrix1([[1,0,1], [0,-2,3]], 2)) #2