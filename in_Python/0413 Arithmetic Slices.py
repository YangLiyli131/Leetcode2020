class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [0] * len(A)
        r = 0
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i] = dp[i-1] + 1
                r += dp[i]
        return r