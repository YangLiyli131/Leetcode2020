class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        seen = []
        row = len(grid)
        col = len(grid[0])
        def dfs(i,j):
            if [i,j] in seen:
                return True
            if not (0 <= i < row and 0 <= j < col and grid[i][j] == grid[r0][c0]):
                return False
            seen.append([i,j])
            if dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1) < 4:
                grid[i][j] = color
            return True
        dfs(r0,c0)
        return grid