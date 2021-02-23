class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        for i in range(1, row):
            for j in range(col):
                cur = matrix[i][j]
                arr = [matrix[i-1][j]]
                if j-1 >= 0:
                    arr.append(matrix[i-1][j-1])
                if j+1 < col:
                    arr.append(matrix[i-1][j+1])
                matrix[i][j] = cur + min(arr)
        return min(matrix[-1])