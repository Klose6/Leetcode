"""
Most frequent subtree sum 508
https://leetcode.com/problems/most-frequent-subtree-sum/tabs/discuss
"""
class node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

val_to_freq = dict()
max_val = 0

def findMostFreqSum(root):
  if not root:
    return 0
  cur_sum = findMostFreqSum(root.left) + findMostFreqSum(root.right) + root.val
  global max_val, val_to_freq
  val_to_freq[cur_sum] = val_to_freq.get(cur_sum, 0) + 1
  if val_to_freq[cur_sum] > max_val:
    max_val = val_to_freq[cur_sum]
  return cur_sum



root = node(5)
root.left = node(2)
root.right = node(-5)

findMostFreqSum(root)
res = [i for i, j in val_to_freq.items() if j == max_val]
print(max_val)
print(val_to_freq)
print(res)
