class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = []
        for i in range(101):
            dp.append([0] * 101)
        dp[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                if dp[i][j] >= 1:
                    dp[i+1][j] += (dp[i][j] - 1) / float(2)
                    dp[i+1][j+1] += (dp[i][j] - 1) / float(2)
        return min(1, dp[query_row][query_glass])