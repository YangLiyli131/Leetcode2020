class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m = []
        for x in matrix:
            t = [0]
            for xi in x:
                t.append(t[-1] + xi)
            self.m.append(t)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r = 0
        for i in range(row1, row2+1):
            rw = self.m[i]
            r += rw[col2+1] - rw[col1]
        return r


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)