"""
437 path sum III
https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation
"""


def pathSum(root, sum):
  if not root: return 0
  return pathSumFrom(root, sum) + pathSumFrom(root.left, sum) + pathSumFrom(root.right, sum)

def pathSumFrom(root, sum): # the path sum contains the current root node
  if not root: return 0
  return (1 if root.val == sum else 0) + pathSumFrom(root.left, sum - root.val) + pathSumFrom(root.right, sum-root.val)