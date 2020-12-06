class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        n = len(rowSum)
        nn = len(colSum)
        res = []
        for i in range(n):
            res.append([0] * nn)
        for i in range(n):
            currow = rowSum[i]
            for j in range(nn):
                curcol = colSum[j]
                m = min(currow, curcol)
                res[i][j] = m
                currow -= m
                curcol -= m
                colSum[j] = curcol
        return res