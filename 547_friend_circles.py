"""
547 friend circles
"""

def findCircleNum(m):
  # dfs
  n = len(m)
  def dfs(m, visited, i):
    for j in range(n):
      if m[i][j] and not visited[j]:
        visited[j] = 1
        dfs(m, visited, j)
  visited = [0] * n
  count = 0
  for i in range(n):
    if not visited[i]:
      count += 1
      dfs(m, visited, i)
  return count


class UnionFind:
  def __init__(self, n):
    self.count = n
    self.size = [1] * n
    self.parent = [i for i in range(n)]

  def find(self, p):
    while p != self.parent[p]:
      self.parent[p] = self.parent[self.parent[p]] # path compression
      p = self.parent[p]
    return p

  def union(self, p, q):
    rootp = self.find(p)
    rootq = self.find(q)
    if rootp == rootq: return # they are already unioned
    # add the smaller size parent to the larger parent to speed up the path compression
    if self.size[rootp] > self.size[rootq]:
      self.parent[rootq] = rootp
      self.size[rootp] += self.size[rootq]
    else:
      self.parent[rootp] = rootq
      self.size[rootq] += self.size[rootp]
    self.count -= 1

  def get_count(self):
    return self.count

def findCircleNum_2(m):
  n = len(m)
  uf = UnionFind(n)
  for i in range(n):
    for j in range(i):
      if m[i][j] == 1:
        uf.union(i, j)
  return uf.get_count()

print(findCircleNum_2([
  [1,1,0],
  [1,1,0],
  [0,0,1]
])) # 2
print(findCircleNum_2([
  [1,1,0],
  [1,1,1],
  [0,1,1]
])) # 1