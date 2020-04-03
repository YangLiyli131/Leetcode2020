class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rowmin = []
        colmax = []
        res = []
        for r in range(len(matrix)):
            cur_row_min = matrix[r][0]
            for c in range(len(matrix[0])):
                if matrix[r][c] < cur_row_min:
                    cur_row_min = matrix[r][c]
            rowmin.append(cur_row_min)

        for c in range(len(matrix[0])):
            cur_col_max = matrix[0][c]
            for r in range(len(matrix)):
                if matrix[r][c] > cur_col_max:
                    cur_col_max = matrix[r][c]
            colmax.append(cur_col_max)
        for i in rowmin:
            if i in colmax:
                res.append(i)
                break
        return res
                
        