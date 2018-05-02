"""
61 rotate list
"""


class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None


def rotate_list(head, k):
	if not head:
		return head
	# number of nodes
	l = 1
	new_head, tail = head
	while tail.next:
		tail = tail.next
		l += 1
	# circle the link
	tail.next = head
	k %= l
	if k:
		for i in range(l - k):
			tail = tail.next
	new_head = tail.next
	tail.next = None
	return new_head
