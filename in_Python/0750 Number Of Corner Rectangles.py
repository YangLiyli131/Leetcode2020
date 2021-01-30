class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        row, col = len(grid), len(grid[0])
        d = {}
        for c in range(col):
            d[c] = set()
        
        if row == 1:
            return 0
        for c in range(col):
            if grid[0][c] == 1:
                d[c].add(0)
        for r in range(1, row):
            idx = []
            for c in range(col):
                if grid[r][c] == 1:
                    idx.append(c)
            if len(idx) < 2:
                continue
            n = len(idx)
            for left in range(n):
                l = idx[left]
                for right in range(left+1, n):
                    ri = idx[right]
                    res += len(d[l].intersection(d[ri]))
            for x in idx:
                d[x].add(r)  
        return res
        