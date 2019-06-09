"""
445 add two numbers II
"""
from utils import ListNode

def add_two_numbers(l1, l2):
  s1, s2 = [], []
  tmp1 = l1
  while tmp1:
    s1.append(tmp1.val)
    tmp1 = tmp1.next
  tmp1 = l2
  while tmp1:
    s2.append(tmp1.val)
    tmp1 = tmp1.next
  head = ListNode(0)
  sum = 0
  while s1 or s2:
    if s1: sum += s1.pop()
    if s2: sum += s2.pop()
    head.val = sum % 10 # assign the current value to the exist node and create a new node for the carry value
    cur = ListNode(sum // 10)
    cur.next = head
    head = cur
    sum //= 10
  return head if head.val != 0 else head.next

l1 = ListNode(7)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(5)
l4 = ListNode(6)
l3.next = l4
print(add_two_numbers(l1, l3).next.val) # 1