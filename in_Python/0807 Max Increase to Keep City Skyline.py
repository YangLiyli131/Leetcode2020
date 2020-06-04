class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        row = len(grid)
        col = len(grid[0])
        rowtop = []
        coltop = []
        for i in range(row):
            cur = 0
            for j in range(col):
                if grid[i][j] > cur:
                    cur = grid[i][j]
            rowtop.append(cur)
        for i in range(col):
            cur = 0
            for j in range(row):
                if grid[j][i] > cur:
                    cur = grid[j][i]
            coltop.append(cur)
        for i in range(row):
            for j in range(col):
                res += min(rowtop[i], coltop[j]) - grid[i][j]
        return res