"""
600 Non-negative integers without consecutive ones
"""


def findIntegers(num):
  """
  a[i]: the number of binary string which doesn't contain consecutive 1s and ends with 0
  b[i]: the number of binary string which doesn't contain consecutive 1s and ends with 1
  we can append either 0 or 1 to a string ends with 0, but can only append 1 to string ends with 0
  then we can get a[i] = a[i-1] + b[i-1], b[i] = a[i-1]
  """
  x, y = 1, 2  # initial status for string with length 1 and 2
  res = 0
  num += 1
  while num:
    if num & 1 and num & 2:
      res = 0
    res += x * (num & 1)
    num >>= 1
    x, y = y, x + y
  return res


def findIntegers1(num):
  """
  we can find there is a Fibonacci series for the non-consecutive 1s in the string
  Assume k=5, then we can divide the range into [0, 1111] and (10000, 10111), any number
  bigger than 11000 will not be valid since it must contain the consecutive 1s
  [0, 1111] is f(4) and (10000, 10111] if f(3), so f(5) = f(4) + f(3)
  we can scan from the left to right, if we meet 1 and its left is 0 and its right has k bits,
  then we can add f(k) to the result since we can reset this bit to 0 and set all the k bits
  as valid string; if its left is 1, then after add the f(k) we need to stop since all the following
  bits will have invalid consecutive 1s. if the loop exit normally, then we need to 1 to the last result
  since the num itself is also valid.
  """
  f = [0] * 32
  f[0], f[1] = 1, 2
  for i in range(2, 32):
    f[i] = f[i - 1] + f[i - 2]
  pre, res, k = 0, 0, 30
  while k >= 0:
    if num & (1 << k):
      res += f[k]
      if pre: return res
      pre = 1
    else:
      pre = 0
    k -= 1
  return res + 1


print findIntegers(5)
print findIntegers1(5)
print findIntegers(0)
print findIntegers1(0)
