class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            cur = matrix[i][j] 
            if cur == target:
                return True
            elif cur < target:
                i += 1
            else:
                j -= 1
        return False
        