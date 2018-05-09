"""
82 remove duplicates from sorted list II
"""


class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None


def remove_duplicates(head):
	if not head or not head.next:
		return head
	dummy = Node(0)
	dummy.next = head
	pre, cur = dummy, head
	while cur:
		while cur.next and cur.next.val == cur.val:
			cur = cur.next
		if pre.next == cur:
			pre = pre.next
		else:
			pre.next = cur.next
		cur = cur.next
	return dummy.next
