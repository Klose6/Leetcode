"""
581 shortest unsorted continous subarray
"""
import sys


def findUnsortedSubarray(nums):
  begin, end = -1, -2
  min_val, max_val = float("inf"), float("-inf")  # sys.maxsize, -sys.maxsize - 1  #
  n = len(nums)
  for i in range(n):
    max_val = max(max_val, nums[i])
    min_val = min(min_val, nums[n - 1 - i])
    if nums[i] < max_val:
      end = i
    if nums[n - 1 - i] > min_val:
      begin = n - 1 - i
  return end - begin + 1


print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # 5
