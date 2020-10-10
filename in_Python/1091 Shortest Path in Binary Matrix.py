class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        q = [[0,0,1]]
        for i,j,d in q:
            if i == N-1 and j == N-1:
                return d
            for x,y in [[i+1,j], [i-1,j], [i+1,j+1], [i-1,j-1], [i,j+1], [i,j-1], [i+1,j-1],[i-1,j+1]]:
                if 0 <= x < N and 0 <= y < N and grid[x][y] == 0:
                    grid[x][y] = 1
                    q.append([x,y,d+1])
        return -1