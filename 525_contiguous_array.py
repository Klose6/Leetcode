"""
525 contiguous array
"""


def findMaxLength(nums):
  if not nums or len(nums) < 2: return 0
  pos = {0: -1} # dict to store the initial prefix sum value position
  count, res = 0, 0
  for i, v in enumerate(nums):
    # since need to find the equal number of 0 and 1, then need some transformation to sum here
    count += 1 if v == 1 else -1
    if count in pos:
      res = max(res, i - pos[count])
    else:
      pos[count] = i
  return res

print(findMaxLength([0, 1])) # 2
print(findMaxLength([0,1,0])) # 2