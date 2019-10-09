"""
863 all node distance K in binary tree
*each node value is unique
"""
import collections


class Node(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


class solution(object):
	def distanceK(self, root, target, K):
		def dfs(node, parent=None):
			if node:
				root.parent = parent
				dfs(root.left, parent=root)
				dfs(root.right, parent=root)

		dfs(root)
		queue = collections.deque([(target, 0)])
		visited = [target]
		while queue:
			if queue[0][1] == K:
				return [node.val for node, d in queue]
			node, d = queue.popleft()
			for nei in (node.parent, node.left, node.right):
				if nei and nei not in visited:
					visited.append(nei)
					queue.append((nei, d + 1))
		return []

	def distanceK1(self, root, target, K):
		conn = collections.defaultdict(list)

		def connect(parent, child):
			if parent and child:
				conn[parent.val].append(child.val)
				conn[child.val].append(parent.val)
			if child.left:
				connect(child, child.left)
			if child.right:
				connect(child, child.right)

		connect(None, root)
		bfs = [target.val]
		seen = set(bfs)
    for i in range(K):
      bfs = [y for x in bfs for y in conn[x] if y not in seen]
			seen |= set(bfs)
		return bfs
