class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [0,1]
        for i in range(2, n+1):
            if i % 2 == 0:
                dp.append(dp[i/2])
            else:
                idx = (i-1) / 2
                dp.append(dp[idx] + dp[idx+1])
        return max(dp)
        