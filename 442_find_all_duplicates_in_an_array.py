"""
442 find all duplicates in an array
"""

def findAllDuplicates(nums):
  """
  for [i] mark the [[i]-1] to negative, then wehen we meet the negative values again, we know it is duplicates
  """
  if not nums: return []
  res = []
  for i, v in enumerate(nums):
    if nums[abs(v) - 1] < 0:
      res.append(abs(v))
    nums[abs(v) - 1] = -nums[abs(v) - 1]
  return res
