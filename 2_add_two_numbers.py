"""
2 Add two numbers
"""


class Node(object):
	def __init__(self, v):
		self.val = v
		self.next = None


class Solution(object):
	def add_two_numbers(self, l1, l2):
		if not l1:
			return l2
		if not l2:
			return l1
		dummy = Node(0)
		p = dummy
		i, j = l1, l2
		carry = 0
		while i or j or carry:
			cur_sum = i.val if i else 0 + j.val if j else 0 + carry
			carry = cur_sum / 10
			p.next = Node(cur_sum % 10)
			p = p.next
			i = i.next if i else None
			j = j.next if j else None
		return dummy.next
