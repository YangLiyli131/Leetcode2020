class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        ave = n
        res = 0
        for i in range(0, 2 * n - 1, 2):
            res += abs(ave - i)
        return res/2