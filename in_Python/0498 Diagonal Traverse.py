class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        res = [matrix[0][0]]
        row = len(matrix)
        col = len(matrix[0])
        endpoints = []
        for j in range(1, col):
            endpoints.append([0,j])
        for i in range(1, row):
            endpoints.append([i,col-1])
        order = 0
        while endpoints:
            end = endpoints.pop(0)
            i = end[0]
            j = end[1]
            cur = []
            while 0 <= i < row and 0 <= j < col:
                if order == 0:
                    cur.append(matrix[i][j])
                else:
                    cur.insert(0, matrix[i][j])
                i += 1
                j -= 1
            order = 1 - order
            for c in cur:
                res.append(c)
        return res