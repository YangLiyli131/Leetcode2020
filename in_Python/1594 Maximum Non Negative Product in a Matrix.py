class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        grid[0][0] = [grid[0][0],grid[0][0]]
        for i in range(1,row):
            cur = grid[i][0]
            pre = grid[i-1][0][0]
            grid[i][0] = [cur*pre, cur*pre]
        for j in range(1, col):
            cur = grid[0][j]
            pre = grid[0][j-1][0]
            grid[0][j] = [cur*pre, cur*pre]
        for i in range(1, row):
            for j in range(1, col):
                num = grid[i][j]
                cur = []
                up = grid[i-1][j]
                for x in up:
                    cur.append(num * x)
                left = grid[i][j-1]
                for x in left:
                    cur.append(num * x)
                grid[i][j] = [min(cur), max(cur)]
        last = grid[-1][-1]
        if last[1] < 0:
            return -1
        return last[1] % (pow(10,9) + 7)