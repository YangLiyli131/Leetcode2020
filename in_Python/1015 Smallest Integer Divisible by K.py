class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K % 2 == 0 or K % 5 == 0:
            return -1
        n = 0
        for i in range(1, K+1):
            n = (n * 10 + 1) % K
            if not n:
                return i