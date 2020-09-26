class Solution(object):
    def dsum (self, n):
        res = 0
        while n != 0:
            res += n % 10
            n /= 10
        return res
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = self.dsum(num)
        return num
        
        