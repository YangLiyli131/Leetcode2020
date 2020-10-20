class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                    continue
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    if i == 0:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1]
                    elif j == 0:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j]
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]