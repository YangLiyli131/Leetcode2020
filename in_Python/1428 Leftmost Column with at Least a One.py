# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        [row, col] = binaryMatrix.dimensions()
        res = col-1
        found = 0
        i,j = 0, col-1
        while i < row and j >= 0:
            if binaryMatrix.get(i,j) == 1:
                found = 1
                res = min(res,j)
                j -= 1
            else:
                i += 1
        if found == 0:
            return -1
        return res