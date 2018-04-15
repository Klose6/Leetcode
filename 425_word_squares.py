"""
425 Word squares
http://www.cnblogs.com/grandyang/p/6006000.html
https://github.com/kamyu104/LeetCode/blob/master/Python/word-squares.py
http://massivealgorithms.blogspot.com/2016/10/leetcode-425-word-squares.html
"""
import collections
import copy

class TrieNode(object):
	def __init__(self):
		self.startswith = []
		self.children = [None] * 26


class Solution(object):
	def __init__(self):
		self.root = TrieNode()
		self.res = []
	def build_trie(self, words):
		# build the trie tree
		for w in words:
			cur = self.root
			for i in w:
				idx = ord(i) - ord("a")
				if not cur.children[idx]:
					cur.children[idx] = TrieNode()
				cur.children[idx].startswith.append(w)
				cur = cur.children[idx]
	def find_by_prefix(self, prefix):
		cur = self.root
		for p in prefix:
			idx = ord(p) - ord("a")
			if not cur.children[idx]:
				return []
			cur = cur.children[idx]
		return cur.startswith
	def search(self, n, curwords):
		if len(curwords) == n:
			self.res.append(copy.deepcopy(curwords))
			return
		prefix = "".join(zip(*curwords)[len(curwords)])
		searchres = self.find_by_prefix(prefix)
		for res in searchres:
			curwords.append(res)
			self.search(n, curwords)
			curwords.pop()
	def word_squares_1(self, words):
		if not words:
			return
		self.build_trie(words)
		n = len(words[0])
		for w in words:
			self.search(n, [w])
		return self.res

	def word_squares_2(self, words):
		if not words:
			return
		n = len(words)
		fulls = collections.defaultdict(list)
		for w in words:
			for i in range(n):
				fulls[w[:i]].append(w)
		squares = []
		def build(square):
			if len(square) == n:
				squares.append(square)
				return
			for w in fulls["".join(zip(*square)[len(square)])]:
				build(square + [w])
		for w in words:
			build([w])
		return squares

s = Solution()
print s.word_squares_2(["wall", "area", "lead", "lady"])
print s.word_squares_1(["wall", "area", "lead", "lady"])