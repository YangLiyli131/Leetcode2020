class Solution(object):
    def helper(self, x):
        res = 0
        while x != 0:
            res += x % 2
            x /= 2
        return res
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        po = [2,3,5,7,11,13,17,19]
        for i in range(L, R+1):
            c = self.helper(i)
            if c in po:
                res += 1
        return res