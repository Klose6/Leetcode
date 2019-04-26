"""
537 complex number multiplication
"""

def complexMultiplication(a, b):
  na = a.split("+")
  nb = b.split("+")
  n = int(na[0]) * int(nb[0]) - int(na[1][:-1]) * int(nb[1][:-1])
  c = int(na[0]) * int(nb[1][:-1]) + int(nb[0]) * int(na[1][:-1])
  return f"{n}+{c}i"


def complexMultiplication_2(a, b):
  a1, a2 = map(int, a[:-1].split("+"))
  b1, b2 = map(int, b[:-1].split("+"))
  return f"{a1*b1-a2*b2}+{a1*b2+a2*b1}i"

print(complexMultiplication_2("1+1i", "1+1i")) # 0+2i
print(complexMultiplication_2("1+-1i", "1+-1i")) # 0+-2i