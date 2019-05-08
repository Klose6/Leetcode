"""
484 find permutation
"""

def findPermutation(s):
  n = len(s)
  nums = [i+1 for i in range(n+1)]
  i = 0
  while i < n:
    if s[i] != "D":
      i += 1
    else: # find the continuous Ds and reverse them
      j = i+1
      while j < n and s[j] == "D":
        j += 1
      # print(f"{i}, {j}")
      nums[i:j+1] = nums[i:j+1][::-1]
      i = j
  return nums

print(findPermutation("D")) # 21
print(findPermutation("ID")) # 213
print(findPermutation("DDIIDI")) # 3214657