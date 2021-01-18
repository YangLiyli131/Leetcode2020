class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        res= 0 
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0 or i == 0:
                    continue
                matrix[i][j] += matrix[i-1][j]
            cur = matrix[i]
            cur = sorted(cur, reverse = True)
            for i in range(col):
                res = max(res, cur[i] * (i+1))
        return res