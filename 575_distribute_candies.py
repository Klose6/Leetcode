"""
575 distribute candies
"""


def maxKindsOfCandies(candies):
  """
  the maximum kinds of candies if the min of
  the half the length of the array and the total kinds of the candies
  """
  return min(len(candies) // 2, len(set(candies)))


print(maxKindsOfCandies([1, 1, 2, 2, 3, 3]))  # 3
print(maxKindsOfCandies([1, 1, 2, 3]))  # 2
