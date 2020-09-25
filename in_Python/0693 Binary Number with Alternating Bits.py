class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pre = n % 2
        n /= 2
        while n != 0:
            cur = n % 2
            if pre == cur:
                return False
            n /= 2
            pre = cur
        return True