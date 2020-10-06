class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        res = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 or grid[i][j] == -1:
                    continue
                if grid[i][j] == 0 and (i == 0 or i == row-1 or j == 0 or j == col-1):
                    continue
                q = []
                q.append([i,j])
                flag = 0
                while len(q) != 0:
                    h = q.pop(0)
                    thisi = h[0]
                    thisj = h[1]
                    for d in directions:
                        nexti = thisi + d[0]
                        nextj = thisj + d[1]
                        if 0 <= nexti < row and 0 <= nextj < col and grid[nexti][nextj] == 0:
                            q.append([nexti,nextj])
                            grid[nexti][nextj] = -1
                            if nexti == 0 or nexti == row-1 or nextj == 0 or nextj == col-1:
                                flag = 1
                if flag == 0:
                    res += 1
        return res
                        
                