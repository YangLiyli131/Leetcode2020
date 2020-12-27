class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        islands = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 1:
                    continue
                q = []
                q.append([i,j])
                grid[i][j] = -1
                cur = []
                while len(q) != 0:
                    h = q.pop(0)
                    cur.append(h)
                    thisi, thisj = h[0],h[1]
                    for d in directions:
                        nexti = thisi + d[0]
                        nextj = thisj + d[1]
                        if 0 <= nexti < row and 0 <= nextj < col:
                            if grid[nexti][nextj] == 1:       
                                q.append([nexti,nextj])
                                grid[nexti][nextj] = -1
                minrow = sys.maxint
                mincol = sys.maxint
                for x in cur:
                    minrow = min(minrow, x[0])
                    mincol = min(mincol, x[1])
                newcur = []
                for x in cur:
                    tmp = [x[0]-minrow, x[1]-mincol]
                    newcur += tmp
                islands.add(tuple(newcur))
        return len(islands)
                    
                    
        