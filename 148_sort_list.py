"""
148 sort list
"""


class Node(object):
	def __int__(self, val):
		self.val = val
		self.next = None


def sort_list(head):
	if not head or not head.next:
		return head
	pre, slow, fast = None, head, head
	while fast and fast.next:
		pre = slow
		slow = slow.next
		fast = fast.next.next
	pre.next = None
	left = sort_list(head)
	right = sort_list(slow)
	return merge(left, right)


def merge(l1, l2):
	dummy = Node(0)
	cur = dummy
	while l1 and l2:
		if l1.val <= l2.val:
			cur.next = l1
			l1 = l1.next
		else:
			cur.next = l2
			l2 = l2.next
		cur = cur.next
	if l1:
		cur.next = l1
	if l2:
		cur.next = l2
	return dummy.next
