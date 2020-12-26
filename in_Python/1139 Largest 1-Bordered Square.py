class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        down = []
        right = []
        up = []
        left = []
        for i in range(row):
            down.append([0] * col)
            right.append([0] * col)
            up.append([0] * col)
            left.append([0] * col)
        for i in range(row):
            for j in range(col):
                if i == 0:
                    up[i][j] = grid[i][j]
                else:
                    if grid[i][j] == 0:
                        up[i][j] = 0
                    else:
                        up[i][j] = up[i-1][j] + grid[i][j]
        for i in range(row-1, -1, -1):
            for j in range(col):
                if i == row-1:
                    down[i][j] = grid[i][j]
                else:
                    if grid[i][j] == 0:
                        down[i][j] = 0
                    else:
                        down[i][j] = down[i+1][j] + grid[i][j]
        for i in range(row):
            for j in range(col-1, -1, -1):
                if j == col-1:
                    right[i][j] = grid[i][j]
                else:
                    if grid[i][j] == 0:
                        right[i][j] = 0
                    else:
                        right[i][j] = right[i][j+1] + grid[i][j]
        for i in range(row):
            for j in range(col):
                if j == 0:
                    left[i][j] = grid[i][j]
                else:
                    if grid[i][j] == 0:
                        left[i][j] = 0
                    else:
                        left[i][j] = left[i][j-1] + grid[i][j]
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                side = min(up[i][j], left[i][j])
                for l in range(side-1, -1, -1):
                    if l < res:
                        break
                    if min(down[i-l][j-l], right[i-l][j-l]) >= l + 1:
                        res = max(res, l+1)
                        break
        return res * res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        