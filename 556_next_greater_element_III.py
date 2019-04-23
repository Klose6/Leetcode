"""
556 next greater element III
"""

def next_greater_element(num):
  s = list(str(num))
  # print(f"s: {s}")
  i = len(s) - 1
  # start from the right most element and find the first element that is smaller than the digit next to it
  while i > 0 and s[i] <= s[i-1]:
      i -= 1
  # print(f"i: {i}")
  # if no such element, which means the nums are sorted reversely, then return -1
  if i == 0: return -1
  # find the smallest digit on right side of i-1 that is greater than i-1
  x, smallest = s[i-1], i
  for j in range(i+1, len(s)):
    if s[j] > s[i-1] and s[j] <= s[smallest]:
      smallest = j
  # swap the sbove found smallest digit with i-1
  s[i-1], s[smallest] = s[smallest], s[i-1]
  # sort the digits after i-1 in ascending order
  s[i:] = sorted(s[i:])
  s = "".join(s)
  # print(f"s: {s}")
  return int(s) if int(s) <= (1<<31-1) else -1

print(next_greater_element(12)) # 21
print(next_greater_element(21)) # -1
print(next_greater_element(4521)) # -1