class Solution(object):
    def sim(self, a, b):
        return a == b
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        res = -1
        for i in range(len(matrix)):
            cur = matrix[i]
            curf = []
            count = 0
            for x in cur:
                curf.append(1 - x)
            for j in range(i, len(matrix)):
                if self.sim(matrix[j], cur) or self.sim(matrix[j], curf):
                    count += 1
            res = max(res, count)
        return res
                    