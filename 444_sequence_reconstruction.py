"""
444 sequence reconstruction
https://www.cnblogs.com/grandyang/p/6032498.html
"""

def sequenceReconstruction(org, seqs):
  if not org or not seqs: return False
  n = len(org)
  pos = [0]*(n+1)
  visited = [0]*(n+1)
  for i, v in enumerate(org):
    pos[v] = i
  existed = False
  count = n-1
  for seq in seqs:
    for i, v in enumerate(seq):
      existed = True
      if 0 >= v or v > n: return False # the number must within 1-n
      if i == 0: continue
      pre, cur = seq[i-1], seq[i] # check the current position and its previous position
      if pos[cur] <= pos[pre]: return False # the previous position must < current position
      if visited[cur] == 0 and pos[pre]+1 == pos[cur]: # if the current as not visited and the previous is its direct neighbor
        visited[cur] = 1
        count -= 1 # mark the current point as verified
  # print(f"count: {count}")
  return count == 0 and existed

print(sequenceReconstruction([1,2,3], [[1,2], [1,3]])) # False
print(sequenceReconstruction([1,2,3], [[1,2], [1,3], [2,3]])) # True