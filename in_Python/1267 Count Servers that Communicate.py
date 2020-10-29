class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        rowdegree = [0] * row
        coldegree = [0] * col
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    rowdegree[i] += 1
                    coldegree[j] += 1
        res = 0
        for i in rowdegree:
            if i > 1:
                res += i
        for i in coldegree:
            if i > 1:
                res += i
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if coldegree[j] > 1 and rowdegree[i] > 1:
                        res -= 1
        return res