"""
527 word abbreviation
"""
import collections


class Solution:
	def word_abbre(self, words):
		def is_unique(prefix, words):
			return sum([w.startswith(prefix) for w in words]) == 1

		def to_abbre(prefix, word):
			tmp = prefix + str(len(word) - len(prefix) - 1) + word[-1]
			return tmp if len(tmp) < len(word) else word

		abbre_to_word = collections.defaultdict(set)
		word_to_abbre = {}
		for word in words:
			abbre_to_word[to_abbre(word[:1], word)].add(word)
		for abbre, conflicts in abbre_to_word.items():
			if len(conflicts) > 1:
				for word in conflicts:
					for i in range(2, len(word)): # start with 2 prefix chars
						if is_unique(word[:i], conflicts):
							word_to_abbre[word] = to_abbre(word[:i], word)
							break
			else:
				word_to_abbre[conflicts.pop()] = abbre
		return word_to_abbre.values()

print(Solution().word_abbre(["like", "god", "me", "internal", "interral"]))
