class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        row = len(grid)
        col = len(grid[0])
        q = collections.deque()
        q.append([0,0])
        visited = set()
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                i,j = q.popleft()
                if i == row-1 and j == col-1:
                    return True
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                x = grid[i][j] 
                if x == 2:
                    if 0 <= j < col and 0 <= i+1 < row and grid[i+1][j] in [2,5,6]:
                        q.append([i+1,j])
                    if 0 <= j < col and 0 <= i-1 < row and grid[i-1][j] in [2,3,4]:
                        q.append([i-1,j])
                elif x == 1:
                    if 0 <= j-1 < col and 0 <= i < row and grid[i][j-1] in [1,4,6]:
                        q.append([i,j-1])
                    if 0 <= j+1 < col and 0 <= i < row and grid[i][j+1] in [1,3,5]:
                        q.append([i,j+1])
                elif x == 3:
                    if 0 <= j < col and 0 <= i+1 < row and grid[i+1][j] in [2,5,6]:
                        q.append([i+1, j])
                    if 0 <= j-1 < col and 0 <= i < row and grid[i][j-1] in [1,4,6]:
                        q.append([i,j-1])
                elif x == 4:
                    if 0 <= j+1 < col and 0 <= i < row and grid[i][j+1] in [1,3,5]:
                        q.append([i, j+1])
                    if 0 <= j < col and 0 <= i+1 < row and grid[i+1][j] in [2,5,6]:
                        q.append([i+1,j])
                elif x == 5:
                    if 0 <= j < col and 0 <= i-1 < row and grid[i-1][j] in [2,3,4]:
                        q.append([i-1,j])
                    if 0 <= j-1 < col and 0 <= i < row and grid[i][j-1] in [1,4,6]:
                        q.append([i,j-1])
                else:
                    if 0 <= j < col and 0 <= i-1 < row and grid[i-1][j] in [2,3,4]:
                        q.append([i-1,j])
                    if 0 <= j+1 < col and 0 <= i < row and grid[i][j+1] in [1,3,5]:
                        q.append([i,j+1])
        return False
                
                    
                    