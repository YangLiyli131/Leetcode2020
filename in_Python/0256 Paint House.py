class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        dp = [[0] * n for _ in range(3)]
        for i in range(3):
            for j in range(n):
                dp[i][j] = costs[j][i]
        for j in range(1, n):
            for i in range(3):
                a = dp[i][j]
                if i == 0:
                    a += min(dp[1][j-1], dp[2][j-1])
                elif i == 1:
                    a += min(dp[0][j-1], dp[2][j-1])
                else:
                    a += min(dp[1][j-1], dp[0][j-1])
                dp[i][j] = a
        r = []
        for i in range(3):
            r.append(dp[i][-1])
        return min(r)