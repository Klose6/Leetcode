"""
kill process

given two lists, first is the process id list and the 2rd is the parent id list,
then given a process id, return all its children process id list
"""
from collections import defaultdict


def killProcess(pid, ppid, kill):
  res = []
  m = defaultdict(list)
  for i in range(len(ppid)):
    m[ppid[i]].append(pid[i])
  q = [kill]
  while q:
    cur = q.pop(0)
    res.append(cur)
    if cur in m:
      q.extend(m[cur])
  return res


print(killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5))  # [5,10]
