from collections import deque


class Solution:
  def __init__(self):
    self.q = deque([])

  def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Number of characters to read (int)
    :rtype: The number of actual characters read (int)
    """
    i = 0
    while i < n:
      if self.q:
        buf[i] = self.q.popleft()
        i += 1
      else:
        buf4 = [""] * 4
        count = read4(buf4)
        if count == 0:
          break
        self.q += buf4[:count]
    return i