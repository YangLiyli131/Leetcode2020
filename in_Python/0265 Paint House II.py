class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        k = len(costs[0])
        dp = [[0] * n for _ in range(k)]
        for i in range(n):
            for j in range(k):
                dp[j][i] = costs[i][j]
        for col in range(1, n):
            for row in range(k):
                cur = dp[row][col]
                pre = []
                for prerow in range(k):
                    if prerow == row:
                        continue
                    pre.append(dp[prerow][col-1])
                dp[row][col] = cur + min(pre)
        r = []
        for i in range(k):
            r.append(dp[i][-1])
        return min(r)