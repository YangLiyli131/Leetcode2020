class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # transpose and swap
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
        i = 0
        j = len(matrix[0]) - 1
        while i < j:
            for r in range(len(matrix)):
                t = matrix[r][i]
                matrix[r][i] = matrix[r][j]
                matrix[r][j] = t
            i += 1
            j -= 1
