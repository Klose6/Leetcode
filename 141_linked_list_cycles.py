"""
141 linked list cycles
"""


class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

def has_cycle(head):
	if not head:
		return False
	slow, fast = head, head.next
	while fast and fast.next:
		if slow == fast:
			return True
		slow = slow.next
		fast = fast.next.next
	return False


n1 = Node(1)
n2 = Node(2)
n1.next = n2
# n2.next = n1
print has_cycle(n1)
