class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 1:
                    continue
                q = []
                v = []
                v.append([i,j])
                q.append([i,j])
                steps = 0
                found = 0
                while len(q) != 0:
                    n = len(q)
                    while n != 0:
                        n -= 1
                        h = q.pop(0)
                        thisi = h[0]
                        thisj = h[1]
                        for d in directions:
                            nexti = thisi + d[0]
                            nextj = thisj + d[1]
                            if 0 <= nexti < row and 0 <= nextj < col and [nexti,nextj] not in v:
                                if grid[nexti][nextj] == 2:
                                    found = 1
                                    break
                                elif grid[nexti][nextj] != 0:
                                    q.append([nexti,nextj])
                                    v.append([nexti,nextj])
                            if found == 1:
                                break
                    steps += 1
                    if found == 1:
                        grid[i][j] = -steps
                        break
                if found == 0:
                    return -1
                res = max(res, abs(steps))
        #print(grid)
        return res
                
                    
        