class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        L1 = len(text1)
        L2 = len(text2)
        dp = []
        curmax = 0
        for i in range(L1+1):
            dp.append([0] * (L2+1))
        for i in range(1,L1+1):
            for j in range(1,L2+1):
                if text1[i-1] == text2[j-1]:
                    cur = dp[i-1][j-1] + 1
                    dp[i][j] = cur
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
                    