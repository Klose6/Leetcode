"""
553 optimal division
"""

def optimal_division(nums):
  if not nums: raise ValueError("Error input")
  # x1/x2/x3/x4 will always equals to (x1/x2)*x3*x4
  res = str(nums[0])
  if len(nums) == 1: return res
  if len(nums) == 2: return f"{res}/{nums[1]}"
  res += f"/({nums[1]}"
  for i in nums[2:]:
    res += f"/{i}"
  res += ")"
  return res

def optimal_division_2(nums):
  if not nums: raise ValueError("Error input")
  A = list(map(str, nums))
  if len(A) <= 2:
    return "/".join(A)
  return f"{A[0]}/({'/'.join(A[1:])})"

print(optimal_division([1000, 100, 10, 2]))
print(optimal_division_2([1000, 100, 10, 2]))