class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        res = 0
        l = high + 1 - low
        if l % 2 == 0:
            return l/2
        else:
            if low % 2 == 1:
                return l/2 + 1
            else:
                return l/2