class Solution(object):
    def check(self, grid, i,j):
        cur = grid[i][j]
        s1 = 0
        s2 = 0
        for ii in range(3):
            s1 += grid[ii][j]
            s2 += grid[i][ii]
        if s1 == 3 * cur or s2 == 3 * cur:
            return True
        if i == j or i + j == 2:
            s1 = 0
            s2 = 0
            for ii in range(3):
                s1 += grid[ii][ii]
                s2 += grid[ii][2-ii]
            if s1 == 3 * cur or s2 == 3 * cur:
                return True
        return False
        
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        grid = []
        for i in range(3):
            grid.append([0] * 3)
        names = ['A','B']
        idx = 1
        for m in moves:
            a = m[0]
            b = m[1]
            cur = 1
            if idx % 2 == 0:
                cur = 5
            idx += 1
            grid[a][b] = cur
            if self.check(grid,a,b):
                if cur == 1:
                    return 'A'
                else:
                    return 'B'
        if idx-1 == 9:
            return 'Draw'
        return 'Pending'
            