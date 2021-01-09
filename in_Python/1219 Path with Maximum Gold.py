class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        row = len(grid)
        col = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(row):
            for j in range(col):
                cur = grid[i][j]
                if cur == 0:
                    continue
                q = collections.deque()
                q.append([i,j,cur, [(i,j)]])
                while q:
                    thisi, thisj, value, path = q.popleft()
                    res = max(res, value)
                    for d in directions:
                        nexti, nextj = thisi + d[0], thisj + d[1]
                        if 0 <= nexti < row and 0 <= nextj < col and (nexti,nextj) not in path and grid[nexti][nextj] != 0:
                            q.append([nexti,nextj, value + grid[nexti][nextj], path + [(nexti,nextj)]])
        return res
                