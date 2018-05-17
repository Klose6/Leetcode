"""
92 reverse linked list
"""


class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None


def reverse_between(head, m, n):
	if not head:
		return
	dummy = Node(0)
	dummy.next = head
	count = 0
	pre = dummy
	while count < m - 1:
		count += 1
		pre = pre.next
	start = pre.next
	count = 0
	print pre.val, start.val
	while count < n - m:
		next = start.next
		start.next = next.next
		next.next = pre.next
		pre.next = next
		pre = next
		count += 1
	return dummy.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
root = reverse_between(n1, 2, 3)
while root:
	print root.val
	root = root.next
