"""
785 if graph bipartie
"""


class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    if not graph: return True
    color = {}

    def dfs(i):
      for j in graph[i]:
        if j not in color:
          color[j] = 1 - color[i]
          if not dfs(j): return False
        else:
          if color[j] == color[i]:
            return False
      return True

    for i in range(len(graph)):
      if i not in color:
        color[i] = 0
        if not dfs(i): return False
    return True
