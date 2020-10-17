class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        tar = 2 * n
        i = 0
        j = int(floor(sqrt(tar)))
        while i+1 < j:
            m = i + (j-i)/2
            if m * m + m <= tar:
                i = m
            else:
                j = m - 1
        if j * j + j <= tar:
            return j
        return i
        