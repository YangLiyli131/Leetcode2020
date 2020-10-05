class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None:
            return 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        row = len(grid)
        col = len(grid[0])
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '0' or grid[r][c] == 'x':
                    continue
                q = []
                q.append([r,c])
                grid[r][c] = 'x'
                while len(q) != 0:
                    h = q.pop(0)
                    thisi = h[0]
                    thisj = h[1]
                    for d in directions:
                        nexti = thisi + d[0]
                        nextj = thisj + d[1]
                        if 0 <= nexti < row and 0 <= nextj < col:
                            if grid[nexti][nextj] == '1':
                                q.append([nexti,nextj])
                                grid[nexti][nextj] = 'x'
                res += 1
        return res