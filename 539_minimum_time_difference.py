"""
539 minimum time difference
"""
from sys import maxsize

def minTimeDifference(times):
  mark = [0] * (24*60) # store all the time in minute in the array
  for t in times:
    hm = t.split(":")
    mark[int(hm[0])*60 + int(hm[1])] = True
  prev, first, last = 0, maxsize, -maxsize
  res = maxsize
  for i in range(24*60):
    if mark[i]:
      if first != maxsize:
        res = min(res, i - prev)
      first = min(first, i)
      last = max(last, i)
      prev = i
  res = min(res, 24*60-last+first) # deal with the overflow - the last adjacent ti the first
  return res

def minTimeDifference_2(times):
  if not times or len(times) < 2: return 0
  def convert(t):
    return int(t[:2]) * 60 + int(t[3:])
  minutes = list(map(convert, times))
  minutes.sort()
  return min([(y-x) % (24*60) for x, y in zip(minutes, minutes[1:] + minutes[:1])])

print(minTimeDifference(["23:59", "00:00"])) # 1
print(minTimeDifference_2(["23:59", "00:00"]))