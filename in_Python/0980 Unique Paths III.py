class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        row, col = len(grid), len(grid[0])
        start = None
        end = None
        n0 = 0

        r = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)
                elif grid[i][j] == 0:
                    n0 += 1

        seen = set()
        seen.add(start)
        paths = [([start], seen)]
        allpaths = []
        
        add = True
        while add:
            add = False
            newpaths = []
            for x in paths:
                a = x[0]
                b = x[1]
                last = a[-1]
                for d in directions:
                    nexti, nextj = last[0] + d[0], last[1] + d[1]
                    if 0 <= nexti < row and 0 <= nextj < col and grid[nexti][nextj] == 0 and (nexti,nextj) not in b:
                        add = True
                        bx = b.copy()
                        bx.add((nexti,nextj))
                        ax = a[:]
                        ax.append((nexti,nextj))
                        newpaths.append([ax,bx])
                allpaths.append(a)
            paths = newpaths
        for p in allpaths:
            if len(p) == n0+1:
                pp = p[-1]
                a,b = pp[0], pp[1]
                if end in [(a+1,b),(a-1,b),(a,b-1),(a,b+1)]:
                    r += 1
        return r
        
        