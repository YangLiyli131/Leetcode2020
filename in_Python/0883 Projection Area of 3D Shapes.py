class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        res = 0
        rowmax = []
        for i in range(r):
            rowmax.append(-1)
        colmax = []
        for j in range(c):
            colmax.append(-1)
        for i in range(r):
            for j in range(c):
                x = grid[i][j] 
                if x != 0:
                    res += 1
                if x > rowmax[i]:
                    rowmax[i] = x
                if x > colmax[j]:
                    colmax[j] = x
        for i in rowmax:
            res += i
        for i in colmax:
            res += i
        return res
        