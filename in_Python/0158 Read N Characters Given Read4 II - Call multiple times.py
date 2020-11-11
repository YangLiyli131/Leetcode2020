# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.q = []
    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.pop(0)
                i += 1
            else:
                buf4 = [''] * 4
                v = read4(buf4)
                if v == 0:
                    return i
                for x in range(v):
                    self.q.append(buf4[x])
        return i