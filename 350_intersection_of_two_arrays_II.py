"""
350 intersection of two arrays II
"""

from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        if not nums1 or not nums2: return []
        c = Counter(nums1)
        res = []
        for i in nums2:
            if i in c and c[i] != 0:
                res.append(i)
                c[i] -= 1
        return res