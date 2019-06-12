"""
439 ternary expression parser
"""

def parser(expression):
  if not expression: raise ValueError("Error Input")
  n = len(expression)
  exp = expression
  # process from the right
  while "?" in exp:
    i = exp.rindex("?")
    exp = exp[:i-1] + exp[i+1:i+2] if exp[i-1] == "T" else exp[i+3:]
  return exp

print(parser("T?2:3")) # 2
print(parser("F?1:T?4:5")) # 4
print(parser("T?T?F:5:3")) # F