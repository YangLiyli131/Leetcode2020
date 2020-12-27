class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            if matrix[i][0] == '1':
                res = 1
                break
        for j in range(col):
            if matrix[0][j] == '1':
                res = 1
                break
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '0':
                    continue
                a = int(matrix[i][j-1])
                b = int(matrix[i-1][j])
                c = int(matrix[i-1][j-1])
                matrix[i][j] = min(a,b,c) + 1
                res = max(res, matrix[i][j])
        print(matrix)
        return res * res