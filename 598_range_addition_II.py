"""
range addition II 598
"""

class Solution:
  def maxCount(self, m, n, ops):
    if not ops or m <=0 or n <= 0:
      return 0
    #row = min([op[0] for op in ops])
    #col = min([op[1] for op in ops])
    x, y = zip(*ops)
    return min(x) * min(y)

print(Solution().maxCount(3,3,[[2,2], [3,3]]))