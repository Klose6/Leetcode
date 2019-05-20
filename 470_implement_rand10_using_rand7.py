"""
470 implement rand10() using rand7()
"""

def rand7():
  pass

def rand10():
  """
  rand7() => and49() => rand40() => rand10()
  """
  res = 40
  while res >= 40:
    res = 7 * (rand7() - 1) + (rand7() - 1)
  return res % 10 + 1