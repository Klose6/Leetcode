"""
565 array nesting
"""


def maxNestedArray(nums):
  if not nums:
    return 0
  res = 0
  for i in range(len(nums)):
    size, j = 0, i
    while nums[j] >= 0:
      # k = nums[j]
      nums[j], j = -1, nums[j]
      # print(f"next j: {j}")
      # j = k
      size += 1
    res = max(res, size)
  return res


print(maxNestedArray([5, 4, 0, 3, 1, 6, 2]))  # 4
