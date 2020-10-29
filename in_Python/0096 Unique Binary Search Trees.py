class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)
        for num in range(2,n+1):
            cur = 0
            for i in range(num):
                cur += dp[i] * dp[num-1-i]
            dp[num] = cur
        return dp[-1]