class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        q = collections.deque()
        v = set()
        for i in range(row):
            found = False
            for j in range(col):
                if grid[i][j] == '*':
                    q.append((i,j))
                    v.add((i,j))
                    found = True
                    break
            if found:
                break
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        step = 0
        while q:
            n = len(q)
            step += 1
            while n != 0:
                n -= 1
                thisi, thisj = q.popleft()
                for d in directions:
                    nexti, nextj = thisi + d[0], thisj + d[1]
                    if 0 <= nexti < row and 0 <= nextj < col and grid[nexti][nextj] == '#':
                        return step
                    if 0 <= nexti < row and 0 <= nextj < col and (nexti,nextj) not in v and grid[nexti][nextj] != 'X':
                        q.append((nexti,nextj))
                        v.add((nexti,nextj))
        return -1