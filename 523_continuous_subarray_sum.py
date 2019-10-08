"""
523 continuous subarray sum
"""

def checkSubarraySum(nums ,k):
  if not nums or len(nums) <= 1: return False # corner cases
  if k == 0 : return False # corner cases
  mods = {0: -1} # need to initialize the dict
  prefix_sum = 0
  for i in range(len(nums)):
    prefix_sum += nums[i]
    prefix_sum %= k # only needs to store the mod k values
    prev = mods.get(prefix_sum)
    # print(f"prev: {prev}, {prefix_sum}")
    if prev != None and i - prev > 1:
        return True
    else:
      mods[prefix_sum] = i
  return False

  class Solution:
    def checkSubarraySum(self, nums, k):
      if not nums: return False
      m = [0]
      s = 0
      for n in nums:
        s += n
        if k: s %= k
        m.append(s)
      seen = set()
      for i in range(len(m) - 3, -1, -1):
        seen.add(m[i + 2])
        if m[i] in seen: return True
      return False

print(checkSubarraySum([23,2,4,6,7], 6)) # True
print(checkSubarraySum([23,2,6,4,7], 6)) # True