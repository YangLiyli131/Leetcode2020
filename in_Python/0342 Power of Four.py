class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sumz = 0
        n = num
        while n != 0 and n != 1:
            x = n % 2
            if x != 0:
                return False
            sumz += 1
            n /= 2
        if n == 0:
            return False
        return sumz % 2 == 0
        