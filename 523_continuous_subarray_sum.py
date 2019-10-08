"""
523 continuous subarray sum
"""


class Solution:
  def checkSubarraySum(self, nums, k):
    if not nums: return False
    # 0 can be divided by any number
    for i in range(len(nums) - 1):
      if nums[i] == 0 and nums[i + 1] == 0:
        return True
    # k should not be 0 now
    if k == 0: return False
    m = {0: -1}
    k = abs(k)
    sum = 0
    for i, n in enumerate(nums):
      sum += n
      sum %= k
      pre = m.get(sum)
      if pre != None and i - pre > 1:
        return True
      if sum not in m:
        m[sum] = i
    return False

class Solution1:
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

#print(checkSubarraySum([23,2,4,6,7], 6)) # True
#print(checkSubarraySum([23,2,6,4,7], 6)) # True