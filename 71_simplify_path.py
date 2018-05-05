"""
71 simplify path
"""


def simplify_path(path):
	stack = []
	for dir in path.split("/"):
		if dir == ".." and stack:
			stack.pop()
		elif dir not in ("..", ".", ""):
			stack.append(dir)
	res = []
	for dir in stack:
		res.append(dir)
	return "/" + "/".join(res) if res else "/"


print simplify_path("/home")
print simplify_path("/a/./b/../../c/")
