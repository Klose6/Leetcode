"""
269 Alien dictionary
"""

from collections import defaultdict, deque


class Solution:
  def alienOrder(self, words):
    if not words: return ""
    chars = set("".join(words))
    graph = defaultdict(set)
    indegree = {x: 0 for x in chars}
    for w in zip(words, words[1:]):
      for a, b in zip(*w):
        if a != b:
          if b not in graph[a]:
            graph[a].add(b)
            indegree[b] += 1
          break
    stack = deque([n for n, c in indegree.items() if c == 0])
    # print(f"stack: {stack}, graph: {graph}")
    res = ""
    while stack:
      cur = stack.popleft()
      res += cur
      for n in graph[cur]:
        indegree[n] -= 1
        if indegree[n] == 0:
          stack.append(n)
    # print(f"res: {res}")
    return res * (set(res) == chars)

print(Solution().alienOrder(["za","zb","ca","cb"]))
print(Solution().alienOrder(["wrt","wrf","er","ett","rftt","te"]))