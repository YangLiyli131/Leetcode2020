class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 0 and n != 1:
            if n % 2 == 1:
                return False
            n /= 2
        if n == 0:
            return False
        return True