"""
314 binary tree vertical order traversal
"""

from collections import defaultdict,deque
class Solution:
    def verticalOrder(self, root):
        if not root: return []
        minVal, maxVal = float("inf"), float("-inf")
        q = deque([(root, 0)])
        d = defaultdict(list)
        while q:
            cur, val = q.popleft()
            minVal, maxVal = min(minVal, val), max(maxVal, val)
            d[val].append(cur.val)
            if cur.left: q.append((cur.left, val-1))
            if cur.right: q.append((cur.right, val+1))
        return [d[i] for i in range(minVal, maxVal+1) if d[i]]