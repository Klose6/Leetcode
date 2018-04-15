"""
Base 7 504
https://leetcode.com/problems/base-7/#/discuss
"""
def getBase7(num):
  sign = "-" if num < 0 else ""
  num = abs(num)
  res = []
  while num>0:
    res.append(str(int(num % 7)))
    num = int(num / 7)
  res.reverse()
  return sign + "".join(res)

def getBase7_1(num):
  if num < 0:
    return "-" + getBase7(-num)
  if 0 <= num < 7:
    return str(num)
  return getBase7(num/7) + getBase7(num%7)

m=101
n=5
print(getBase7(m), getBase7_1(m))
print(getBase7(n), getBase7_1(n))