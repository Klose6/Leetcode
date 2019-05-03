"""
495 teemo attacking
"""
#https://discuss.leetcode.com/topic/77360/python-solution-for-teemo
def totalAttackingTime(timeSeries, duration):
  if not timeSeries or duration <= 0:
      return 0
  res = 0
  next = timeSeries[0]
  for i in timeSeries:
      if next <= i:
          res += duration
          next = i+duration
      else:
          res += duration - (next - i)
          next = max(next, i + duration)
  return res

def totalAttackingTime2(timeSeries, duration):
  if not timeSeries or duration <= 0:
    return 0
  res = duration * len(timeSeries)
  for i in range(1, len(timeSeries)):
    res -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
  return res

print(totalAttackingTime([1,2], 2)) # 3
print(totalAttackingTime2([1,2], 2)) # 3