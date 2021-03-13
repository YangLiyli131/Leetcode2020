class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        row,col = len(grid), len(grid[0])
        dp_left = [[0] * col for _ in range(row)]        
        for i in range(row):
            if grid[i][0] == 'E':
                num = 1
            else:
                num = 0
            for j in range(1, col):
                if grid[i][j] == 'W':
                    num = 0
                elif grid[i][j] == 'E':
                    dp_left[i][j] = num
                    num += 1
                else:
                    dp_left[i][j] = num
        print(dp_left)
        
        dp_right = [[0] * col for _ in range(row)]        
        for i in range(row):
            if grid[i][-1] == 'E':
                num = 1
            else:
                num = 0
            for j in range(col-2,-1,-1):
                if grid[i][j] == 'W':
                    num = 0
                elif grid[i][j] == 'E':
                    dp_right[i][j] = num
                    num += 1
                else:
                    dp_right[i][j] = num
        print(dp_right)
        
        dp_down = [[0] * col for _ in range(row)]        
        for j in range(col):
            if grid[0][j] == 'E':
                num = 1
            else:
                num = 0
            for i in range(1,row):
                if grid[i][j] == 'W':
                    num = 0
                elif grid[i][j] == 'E':
                    dp_down[i][j] = num
                    num += 1
                else:
                    dp_down[i][j] = num
        print(dp_down)
        
        dp_up = [[0] * col for _ in range(row)]        
        for j in range(col):
            if grid[-1][j] == 'E':
                num = 1
            else:
                num = 0
            for i in range(row-2,-1,-1):
                if grid[i][j] == 'W':
                    num = 0
                elif grid[i][j] == 'E':
                    dp_up[i][j] = num
                    num += 1
                else:
                    dp_up[i][j] = num
        print(dp_up)
        r = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    s = dp_left[i][j] + dp_right[i][j] + dp_up[i][j] + dp_down[i][j]
                    r = max(r,s)
        return r
                