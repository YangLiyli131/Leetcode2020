class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == None:
            return False
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        rid = 0
        for r in range(row):
            if matrix[r][col-1] >= target:
                rid = r
                break
        r = matrix[rid]
        i = 0
        j = col - 1
        while i <= j:
            m = i + (j-i) / 2
            if r[m] == target:
                return True
            elif r[m] > target:
                j = m - 1
            else:
                i = m + 1
        return False
        