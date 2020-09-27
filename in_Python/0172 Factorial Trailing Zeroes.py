class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1, n+1):
            c = 0
            while i % 5 == 0:
                c += 1
                i /= 5
            res += c
        return res
                
        