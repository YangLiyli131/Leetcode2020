class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        L1 = len(A)
        L2 = len(B)
        dp = []
        res = 0
        for i in range(L1+1):
            dp.append([0] * (L2+1))
        for i in range(1, L1+1):
            for j in range(1,L2+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
        return res