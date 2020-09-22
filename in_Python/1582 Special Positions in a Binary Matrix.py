class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row_ones = []
        col_ones = []
        for i in range(len(mat)):
            row_ones.append(0)
        for j in range(len(mat[0])):
            col_ones.append(0)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):        
                if mat[i][j] == 1 and row_ones[i] == 1 and col_ones[j] == 1:
                    res += 1
        return res