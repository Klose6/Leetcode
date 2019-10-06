"""
282 expression add operators
"""


class Solution:
  def addOperators(self, num: str, target: int) -> List[str]:
    def backtracking(idx, path, value, prev):
      if idx == len(num) and value == target:
        rtn.append(path)
        return
      for i in range(idx + 1, len(num) + 1):
        tmp = int(num[idx: i])
        if i == idx + 1 or (i > idx + 1 and num[idx] != '0'):
          if prev is None:
            backtracking(i, num[idx: i], tmp, tmp)
          else:
            backtracking(i, path + '+' + num[idx: i], value + tmp, tmp)
            backtracking(i, path + '-' + num[idx: i], value - tmp, -tmp)
            backtracking(i, path + '*' + num[idx: i], value - prev + prev * tmp, prev * tmp)

    rtn = []
    backtracking(0, "", 0, None)
    return rtn