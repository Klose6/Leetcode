"""
25 reverse nodes in k group
"""


class Node(object):
	def __init__(self, v):
		self.val = v
		self.next = None


def rever_nodes_in_group(head, k):
	if not head:
		return
	n, cur = 0, head
	while cur:
		n += 1
		cur = cur.next
	# print "n:" + str(n)
	dummy = Node(0)
	dummy.next = head
	prev, cur = dummy, head
	for i in range(n / k):
		for j in range(k - 1):
			next = cur.next.next
			cur.next.next = prev.next
			prev.next = cur.next
			cur.next = next
		prev = cur
		cur = cur.next
	return dummy.next


n1 = Node(1)
n2 = Node(2)
n1.next = n2
print rever_nodes_in_group(n1, 2).val
