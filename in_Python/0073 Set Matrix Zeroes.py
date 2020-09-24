class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    for ri in range(row):
                        if matrix[ri][c] != 0:
                            matrix[ri][c] = 'x'
                    for ci in range(col):
                        if matrix[r][ci] != 0:
                            matrix[r][ci] = 'x'
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 'x':
                    matrix[r][c] = 0