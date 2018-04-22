"""
30 substring with concatenation of all words
"""
from collections import defaultdict


def find_substring(s, words):
	if not s or not words:
		return []
	counts = defaultdict(int)
	total_count = len(words)
	for w in words:
		counts[w] += 1
	wl = len(words[0])
	res = []
	for i in range(wl):
		cur_dict = defaultdict(int)
		cur_count = 0
		j = left = i
		while j <= len(s) - wl:
			cur_str = s[j:j + wl]
			if cur_str in counts:
				cur_dict[cur_str] += 1
				if cur_dict[cur_str] <= counts[cur_str]:
					cur_count += 1
				else:
					while cur_dict[cur_str] > counts[cur_str]:
						str1 = s[left:left + wl]
						cur_dict[str1] -= 1
						if cur_dict[str1] < counts[cur_str]:
							cur_count -= 1
						left += wl
				if cur_count == total_count:
					res.append(left)
					cur_dict[s[left:left + wl]] -= 1
					left += wl
					cur_count -= 1
			else:
				cur_dict = defaultdict(int)
				cur_count = 0
				left = j + wl
			j += wl
		return res


print find_substring("barfoothefoobarman", ["foo", "bar"])  # [0,9]
print find_substring("wordgoodstudentgoodword", ["word", "student"])  # []
