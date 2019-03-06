"""
581 shortest unsroted continous subarray
"""
import sys


def findUnsortedSubarray(nums):
  begin, end = -1, -2
  min, max = sys.maxsize, -sys.maxsize - 1  # float("inf"), float("-inf")
  n = len(nums)
  for i in range(n):
    if nums[i] > max: max = nums[i]
    if nums[n - 1 - i] < min: min = nums[n - 1 - i]
    if nums[i] < max:
      end = i
    if nums[n - 1 - i] > min:
      begin = n - 1 - i
  return end - begin + 1


print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # 5
