class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * 5
        while n != 1:
            for i in range(1,5):
                dp[i] += dp[i-1]
            n -= 1
        return sum(dp)