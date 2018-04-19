"""
19 remove nth node from end of list
"""


class Node(object):
	def __init__(self, v):
		self.val = v
		self.next = None


def remove_th_from_end(head, n):
	if not head or n < 0:
		return
	fast = slow = head
	for _ in range(n):
		fast = fast.next
	if not fast:
		return head.next
	while fast.next:
		fast = fast.next
		slow = slow.next
	slow.next = slow.next.next
	return head


def remove_nth_from_end(head, n):
	def index(node):
		if not node:
			return 0
		i = index(node.next) + 1
		if i > n:
			node.next.val = node.val
		return i

	index(head)
	return head.next
