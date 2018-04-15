from collections import defaultdict

def findMinHeightTree(n, edges):
  neighbors = defaultdict(set)
  for i, j in edges:
    neighbors[i].add(j)
    neighbors[j].add(i)
  def maxpath(v, visited):
    visited.add(v)
    paths = [maxpath(w, visited) for w in neighbors[v] if w not in visited]
    path = max(paths or [[]], key=len)
    path.append(v)
    return path
  path = maxpath(0, set())
  print(path)
  path = maxpath(path[0], set())
  m = len(path)
  print((m-1)//2, m//2+1)
  return path[(m-1)//2:m//2+1]

edges = [(0,1), (1,2)]
print(findMinHeightTree(3, edges))