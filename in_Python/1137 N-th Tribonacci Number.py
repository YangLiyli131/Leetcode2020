class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(1)
        if n < 3:
            return dp[n]
        for i in range(3, n+1):
            nn = dp[i-1] + dp[i-2] + dp[i-3]
            dp.append(nn)
        return dp[n]
        