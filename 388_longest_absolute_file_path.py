"""
388 Longest absolute file path
https://leetcode.com/problems/longest-absolute-file-path/
https://leetcode.com/problems/longest-absolute-file-path/discuss/86619/Simple-Python-solution
https://leetcode.com/problems/longest-absolute-file-path/discuss/86615/9-lines-4ms-Java-solution
"""

class Solution:
	def longest_path(self, input):
		if not input:
			return 0
		maxlen = 0
		pathlen = {0: 0}
		for line in input.splitlines():
			name = line.lstrip("\t")
			depth = len(line) - len(name)
			if "." in line:
				maxlen = max(maxlen, pathlen[depth] + len(name))
			else:
				pathlen[depth+1] = pathlen[depth] + len(name) + 1
		return maxlen

a = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print Solution().longest_path(a)