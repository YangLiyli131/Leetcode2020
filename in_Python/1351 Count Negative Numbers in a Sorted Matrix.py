class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(grid[0])-1
        while j >= 0 and i < len(grid):
            if grid[i][j] < 0:
                res += len(grid) - i
                j -= 1
            else:
                i += 1
        return res
        