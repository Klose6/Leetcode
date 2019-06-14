"""
437 path sum III
https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation
"""


def pathSum(root, sum):
  if not root: return 0
  return pathSumFrom(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum)

def pathSumFrom(root, sum): # the path sum contains the current root node
  if not root: return 0
  return (1 if root.val == sum else 0) + pathSumFrom(root.left, sum - root.val) + \
         pathSumFrom(root.right, sum-root.val)

from collections import defaultdict
res = 0
def pathSum2(root, sum):
  if not root: return 0
  cache = defaultdict(int)
  cache[0] = 1
  helper(root, sum, 0, cache)
  return res

def helper(node, target, current, cache):
  global res
  complement = node.val + current - target
  if complement in cache:
    res += cache.get(complement)
  cache[node.val+current] += 1
  helper(node.left, target, node.val+current, cache)
  helper(node.right, target, node.val+current, cache)
  cache[node.val+current] -= 1