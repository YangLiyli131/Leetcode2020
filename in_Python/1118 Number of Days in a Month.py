class Solution(object):
    def isL(self, y):
        return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        if self.isL(Y) and M == 2:
            return 29
        x = [1,3,5,7,8,10,12]
        if M in x:
            return 31
        if M == 2:
            return 28
        return 30
        