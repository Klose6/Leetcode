"""
208 implement trie
"""
import collections
class TrieNode:
	def __init__(self):
		self.isword = False
		self.children = collections.defaultdict(TrieNode)

class Trie(object):
	def __init__(self):
		self.root = TrieNode()
	def insert(self, word):
		cur = self.root
		for w in word:
			cur = cur.children[w]
		cur.isword=True
	def search(self, word):
		cur=self.root
		for w in word:
			cur = cur.children.get(w)
			if not cur:
				return False
		return cur.isword
	def startswith(self, word):
		cur=self.root
		for w in word:
			cur = cur.children.get(w)
			if not cur:
				return False
		return True