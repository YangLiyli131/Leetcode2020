from functools import lru_cache as cache
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        @cache(None)
        def dfs(r, c1, c2):
            if r == m: return 0
            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
            ans = 0
            for nc1 in range(c1 - 1, c1 + 2):
                for nc2 in range(c2 - 1, c2 + 2):
                    if nc1 >= 0 and nc1 < n and nc2 >= 0 and nc2 < n:
                        ans = max(ans, dfs(r + 1, nc1, nc2))
            return ans + cherries
        
        return dfs(0, 0, n - 1)