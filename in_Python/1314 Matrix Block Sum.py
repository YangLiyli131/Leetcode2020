class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        row = len(mat)
        col = len(mat[0])
        dp = []
        for i in range(row+1):
            dp.append([0] * (col+1))
        for i in range(row):
            for j in range(col):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] + mat[i][j] - dp[i][j]
        res = []
        for i in range(row):
            res.append([0] * col)
        for i in range(row):
            for j in range(col):
                r1 = max(0, i - K)
                c1 = max(0, j - K)
                r2 = min(row, i + K + 1)
                c2 = min(col, j + K + 1)
                res[i][j] = dp[r1][c1] + dp[r2][c2] - dp[r1][c2] - dp[r2][c1]
        return res