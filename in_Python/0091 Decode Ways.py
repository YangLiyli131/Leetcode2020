class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if s == None or N == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * (N+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, N+1):
            first = int(s[i-1:i])
            sec = int(s[i-2:i])
            if 0 < first <= 9:
                dp[i] += dp[i-1]
            if 10 <= sec <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
        