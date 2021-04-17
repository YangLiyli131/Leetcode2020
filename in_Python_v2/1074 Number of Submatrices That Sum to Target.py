from collections import defaultdict
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        ps = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + matrix[i-1][j-1]
        res = 0
        for r1 in range(1, row+1):
            for r2 in range(r1, row+1):
                h = defaultdict(int)
                h[0] = 1
                for c in range(1, col+1):
                    curs = ps[r2][c] - ps[r1-1][c]
                    res += h[curs - target]
                    h[curs] += 1
        return res
        