class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        r = 0
        while n != 0:
            r += n % k
            n /= k
        return r