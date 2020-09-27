class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return res
        pac_mat = []
        atl_mat = []
        row, col = len(matrix), len(matrix[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        for r in range(row):
            t = []
            tt = []
            for c in range(col):
                t.append(0)
                tt.append(0)
            pac_mat.append(tt)
            atl_mat.append(t)
        for r in range(row):
            for c in range(col):
                if r == 0 or c == 0:
                    pac_mat[r][c] = 1
                if r == row - 1 or c == col - 1:
                    atl_mat[r][c] = 1
        for i in range(row):
            for j in range(col):
                q = collections.deque()
                q.append((i,j))
                while q:
                    c = q.popleft()
                    curi, curj = c[0], c[1]
                    for di in directions:
                        nexti = curi + di[0]
                        nextj = curj + di[1]
                        if 0 <= nexti < row and 0 <= nextj < col:
                            if matrix[nexti][nextj] >= matrix[curi][curj] and pac_mat[nexti][nextj] == 0 and pac_mat[curi][curj] == 1:
                                q.append((nexti,nextj))
                                pac_mat[nexti][nextj] = 1
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                q = collections.deque()
                q.append((i,j))
                while q:
                    c = q.popleft()
                    curi, curj = c[0], c[1]
                    for di in directions:
                        nexti = curi + di[0]
                        nextj = curj + di[1]
                        if 0 <= nexti < row and 0 <= nextj < col:
                            if matrix[nexti][nextj] >= matrix[curi][curj] and atl_mat[nexti][nextj] == 0 and atl_mat[curi][curj] == 1:
                                q.append((nexti,nextj))
                                atl_mat[nexti][nextj] = 1
        for i in range(row):
            for j in range(col):
                if pac_mat[i][j] == 1 and atl_mat[i][j] == 1:
                    res.append([i,j])
        return res
                                    
                    
                        
                
                