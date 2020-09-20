class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        res = 0
        length = len(mat)
        for i in range(length):
            res += mat[i][i]
            res += mat[i][length-i-1]
        if length % 2 == 0:
            return res
        else:
            return res - mat[length/2][length/2]
        