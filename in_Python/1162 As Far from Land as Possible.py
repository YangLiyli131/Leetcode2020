class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        res = -1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        lands = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    lands.append([i,j])
        level = -1
        if len(lands) == row * col or len(lands) == 0:
            return level
        while lands:
            n = len(lands)
            while n != 0:
                n -= 1
                h = lands.pop(0)
                thisi = h[0]
                thisj = h[1]
                for d in directions:
                    nexti = thisi + d[0]
                    nextj = thisj + d[1]
                    if 0 <= nexti < row and 0 <= nextj < col and grid[nexti][nextj] == 0:
                        grid[nexti][nextj] = 1
                        lands.append([nexti,nextj])
            level += 1
        return level
                