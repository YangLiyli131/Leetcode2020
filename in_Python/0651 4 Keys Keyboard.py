class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 6:
            return N
        dp = list(range(1,7))
        for i in range(7,N+1):
            t = -1
            for j in range(1,i-2):
                d = i - j - 2
                t = max(t, dp[j] * d)
            dp.append(t)
        return dp[-1]