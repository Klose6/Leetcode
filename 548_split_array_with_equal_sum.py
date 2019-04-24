"""
548 split array with equal sum
"""

def split_array(nums):
  if not nums or len(nums) < 7: return False
  n = len(nums)
  sums = [0] * n
  sums[0] = nums[0]
  for i in range(1, n): # compute the prefix sum for range sum
    sums[i] = sums[i-1] + nums[i]
  print(f"sums: {sums}")
  for j in range(3, n-3): # start from the middle and check the left and right side to make the time complexity O(n2)
    s = set()
    for i in range(1, j-1):
      if sums[i-1] == sums[j-1] - sums[i]:
        s.add(sums[i-1])
    for k in range(j+1, n-1):
      if (sums[k-1] - sums[j] == sums[n-1] - sums[k]) and (sums[k-1] - sums[j] in s):
        print(f"k: {k}, sum: {sums[k-1] - sums[j]}")
        return True
  return False

print(split_array([1,2,1,2,1,2,1])) # True