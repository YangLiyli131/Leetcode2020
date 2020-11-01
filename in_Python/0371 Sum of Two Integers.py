class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0: return b
        elif b == 0: return a
        mask = 0xffffffff
        while b:
            c = a & b
            a = (a ^ b) & mask 
            b = (c << 1) & mask 
        if (a >> 31) & 1:
            return ~(a ^ mask)
        return a