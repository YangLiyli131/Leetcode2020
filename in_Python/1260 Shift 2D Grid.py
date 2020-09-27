class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        row = len(grid)
        col = len(grid[0])
        while k != 0:
            k -= 1
            lastcol = []
            for i in range(row):
                lastcol.append(grid[i][col-1])
            for i in range(row):
                for j in range(col-1, 0, -1):
                    grid[i][j] = grid[i][j-1]
            grid[0][0] = lastcol[-1]
            idx = 0
            for i in range(1, row):
                grid[i][0] = lastcol[idx]
                idx += 1
        return grid