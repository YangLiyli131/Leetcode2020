class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        res = 0
        row = len(matrix)
        col = len(matrix[0])
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    continue
                else:
                    matrix[i][j] = 1 + min(min(matrix[i-1][j-1], matrix[i-1][j]), matrix[i][j-1])
        #print(matrix)
        for i in range(row):
            for j in range(col):
                res += matrix[i][j]
        return res