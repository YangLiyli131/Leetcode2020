class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        row, col = n,n
        res = []
        for i in range(n):
            res.append([0] * n)
        left, right = 0, col-1
        up, down = 0, row-1
        num = 1
        while num <= n*n:
            for i in range(left, right+1):
                if num <= n*n:
                    res[up][i] = num
                    num += 1
            for i in range(up+1, down):
                if num <= n*n:
                    res[i][right] = num
                    num += 1
            for i in range(right, left-1, -1):
                if num <= n*n:
                    res[down][i] = num
                    num += 1
            for i in range(down-1, up, -1):
                if num <= n*n:
                    res[i][left] = num
                    num += 1
            up += 1
            left += 1
            right -= 1
            down -= 1
        return res
            