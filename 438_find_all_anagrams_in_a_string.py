"""
438 find all anagrams in a string
"""

from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        if not s or not p or len(s) < len(p): return []
        res = []
        cp = Counter(p)
        lenp = len(p)
        sp = Counter(s[:lenp-1])
        for i, c in enumerate(s[lenp-1:], lenp-1):
            sp[c] += 1
            if sp == cp:
                res.append(i-lenp+1)
            sp[s[i-lenp+1]] -= 1
            if sp[s[i-lenp+1]] == 0:
                del sp[s[i-lenp+1]]
        return res