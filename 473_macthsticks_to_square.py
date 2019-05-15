"""
473 matchsticks to square
"""

def makeSquare(nums):
  if not nums or len(nums) < 4: return False
  r = sum(nums)
  e = r // 4
  if e * 4 != r: return False
  target = [e] * 4 # using dfs to find whether there is a match
  nums.sort(reverse=True)
  def dfs(nums, pos, target):
    if pos == len(nums): return True
    for i in range(4):
      if target[i] >= nums[pos]:
        target[i] -= nums[pos]
        if dfs(nums, pos+1, target): return True
        target[i] += nums[pos]
    return False
  return dfs(nums, 0, target)


print(makeSquare([1,1,2,2,2])) #true
print(makeSquare([3,3,3,3,4])) #false