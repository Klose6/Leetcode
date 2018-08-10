"""
206 reverse linked list
"""


class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None


def reverse_linked_list(head):
	if not head:
		return head
	dummy = Node(0)
	pre, cur = dummy, head
	while cur:
		next = cur.next
		cur.next = pre.next
		pre.next = cur
		cur = next
	return dummy.next


def reverse_linked_list1(head):
	return reverse_helper(head, None)


def reverse_helper(head, new_head):
	if not head:
		return new_head
	next = head.next
	head.next = new_head
	return reverse_helper(next, head)


n1 = Node(1)
n2 = Node(2)
n1.next = n2
# print reverse_linked_list(n1).val
print reverse_linked_list1(n1).val
