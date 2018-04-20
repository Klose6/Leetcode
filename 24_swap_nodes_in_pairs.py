"""
24 swap node in pairs
"""


class Node(object):
	def __init__(self, v):
		self.val = v
		self.next = None


def swap_pairs(head):
	if not head or not head.next:
		return head
	n = head.next
	head.next = swap_pairs(head.next.next)
	n.next = head
	return n


def swap_pairs2(head):
	pre = Node(0)
	pre.next = head
	while pre.next and pre.next.next:
		a = pre.next
		b = a.next
		pre.next, b.next, a.next = b, a, b.next
		pre = a
	return pre.next
