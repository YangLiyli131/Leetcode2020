class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        j = num/2
        while i < j:
            m = i + (j-i) / 2
            x = m * m
            if x == num:
                return True
            elif x < num:
                i = m + 1
            else:
                j = m - 1
        return i * i == num