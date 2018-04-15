"""
Maximum index sum of two lists 599
"""

class Solution:
  def minIndexSumOfTwoLists(self, a, b):
    if not a or not b:
      return []
    a_index = {v:i for i, v in enumerate(a)}
    min_sum = 1e9
    res =[]
    for j, v in enumerate(b):
      cur_index = a_index.get(v, 1e9)
      if cur_index < min_sum:
        min_sum = cur_index + j
        res = [v]
      elif cur_index + j == min_sum:
        res.append(v)
    return res

a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
b = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(Solution().minIndexSumOfTwoLists(a,b))