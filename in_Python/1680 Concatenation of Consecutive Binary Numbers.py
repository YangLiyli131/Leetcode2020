class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        size = 0
        res = 0
        for i in range(1, n+1):
            if i & (i-1) == 0:
                size += 1
            res = ((res << size) | i) % (1000000007)
        return res