"""
592 Fraction addition and subtraction
"""
import re
import math


def fractionAddition(expression):
  if not expression:
    raise Exception("Invalid input")
  # get the list of all integers
  ints = map(int, re.findall("[+-]?\d+", expression))
  A, B = 0, 1
  for a in ints:
    b = next(ints)
    # print(f"b: {b}")
    A = A * b + a * B
    B *= b
    g = math.gcd(A, B)
    A //= g
    B //= g
  return f"{A}/{B}"


print(fractionAddition("1/3-1/2"))  # -1/6
