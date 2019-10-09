"""
721 accounts merge
"""

from collections import defaultdict


class Solution:
  def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    if not accounts: return []
    email_to_name = {}
    parents = {}

    def find(i):
      while i != parents[i]:
        i = parents[i]
      return i

    def union(i, j):
      parents[find(i)] = find(j)

    # build the graph
    for account in accounts:
      name = account[0]
      for email in account[1:]:
        if email not in parents:
          parents[email] = email
        email_to_name[email] = name
        union(email, account[1])
    # add all the child nodes to its root node
    tree = defaultdict(list)
    for email in parents:
      tree[find(email)].append(email)
    return [[email_to_name[email]] + sorted(vals) for email, vals in tree.items()]
