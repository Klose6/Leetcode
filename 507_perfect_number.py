"""
Perfect Number 507
https://leetcode.com/problems/perfect-number/#/solution
"""
from math import sqrt

def perfect(num):
  if num == 1:
    return False
  res = 1
  for i in range(2, int(sqrt(num)+1)):
    if num % i == 0:
      res += i + num / i
  return res == num

def perfect_2(num):
  if num == 1:
    return False
  return sum([i for i in range(1, num) if num%i == 0]) == num

n = 28
print(perfect(n))
print(perfect_2(n))