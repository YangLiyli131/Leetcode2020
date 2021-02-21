class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        r = 0
        while X < Y:
            r += Y % 2 + 1
            Y = (Y + 1) / 2
        return r + X - Y