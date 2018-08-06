"""
141 linked list cycles
"""


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
