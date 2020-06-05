class Solution(object):
    def helper(self,i,j,row,col,grid):
        c = 4
        if i-1 >= 0 and grid[i-1][j] == 1:
            c -= 1
        if j-1 >= 0 and grid[i][j-1] == 1:
            c -= 1
        if i+1 < row and grid[i+1][j] == 1:
            c -= 1
        if j+1 < col and grid[i][j+1] == 1:
            c -= 1
        return c
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += self.helper(i,j,len(grid),len(grid[0]),grid)
        return res
        