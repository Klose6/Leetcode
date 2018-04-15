"""
determine a graph is Bipartite
http://www.geeksforgeeks.org/bipartite-graph/
"""
from Queue import Queue

def bipartite(adj):
  if not adj:
    return True
  V = len(adj)
  color = [-1] * V
  q = Queue()
  q.put(0)
  color[0] = 0
  while not q.empty():
    c = q.get()
    if adj[c][c]:
      return False
    for j in range(V):
      if adj[c][j] == 1:
        if color[j] == color[c]:
          return False
        elif color[j] == -1:
          color[j] = 1 - color[c]
          q.put(j)
  return True

adj = [[0,1,0,1], [1,0,1,0],[0,1,0,1],[1,0,1,0]]
print bipartite(adj)