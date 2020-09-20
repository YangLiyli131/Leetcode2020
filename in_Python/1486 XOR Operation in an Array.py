class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res = start
        while n != 1:
            start += 2
            res = res ^ start
            n -= 1
        return res