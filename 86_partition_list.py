"""
86 partition list
"""


class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None


def partition_list(head, x):
	if not head or not head.next:
		return
	h1, h2 = Node(0), Node(0)
	p1, p2 = h1, h2
	start = head
	while start:
		if start.val < x:
			p1.next = start
			p1 = p1.next
		else:
			p2.next = start
			p2 = p2.next
		start = start.next
	p2.next = None
	p1.next = h2.next
	return h1.next
