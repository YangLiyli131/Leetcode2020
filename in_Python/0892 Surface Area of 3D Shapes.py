class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        rowmax = []
        colmax = []
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x = grid[i][j]
                if x != 0:
                    res += 2
                    res += 4 * x
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x = grid[i][j]
                if x != 0:
                    for di in directions:
                        nexti = i + di[0]
                        nextj = j + di[1]
                        if 0 <= nexti < len(grid) and 0 <= nextj < len(grid[0]):
                            if grid[nexti][nextj] != 0:
                                res -= min(grid[i][j], grid[nexti][nextj])
        return res
        