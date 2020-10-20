class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        row = len(matrix)
        col = len(matrix[0])
        up, down = 0, row-1
        left,right = 0, col-1
        res = []
        while len(res) != row * col:
            for i in range(left, right+1):
                if len(res) != row * col:
                    res.append(matrix[up][i])
            for i in range(up+1, down):
                if len(res) != row * col:
                    res.append(matrix[i][right])
            for i in range(right, left-1,-1):
                if len(res) != row * col:
                    res.append(matrix[down][i])
            for i in range(down-1, up,-1):
                if len(res) != row * col:
                    res.append(matrix[i][left])
            up += 1
            left += 1
            right -= 1
            down -= 1
        return res