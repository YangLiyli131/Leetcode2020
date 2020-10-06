class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        if grid == None:
            return res
        if len(grid) == 0 or len(grid[0]) == 0:
            return res
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 or grid[i][j] == -1:
                    continue
                q = []
                size = 0
                grid[i][j] = -1
                q.append([i,j])
                while len(q) != 0:
                    h = q.pop(0)
                    size += 1
                    thisi = h[0]
                    thisj = h[1]
                    for d in directions:
                        nexti = thisi + d[0]
                        nextj = thisj + d[1]
                        if 0 <= nexti < row and 0 <= nextj < col and grid[nexti][nextj] == 1:
                            q.append([nexti,nextj])
                            grid[nexti][nextj] = -1
                res = max(res,size)
        return res
                    