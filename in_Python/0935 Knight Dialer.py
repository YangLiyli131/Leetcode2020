class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        x0 = x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = 1
        for i in range(n-1):
            x0,x1,x2,x3,x4,x5,x6,x7,x8,x9 = x4 + x6,\
            x6 + x8, x7 + x9, x4 + x8, x3 + x0 + x9, 0, x1 + x7 + x0, x2 + x6, x1 + x3, x4 + x2
        return (x1+x2+x3+x4+x5+x6+x7+x8+x9+x0) % (pow(10,9)+7)