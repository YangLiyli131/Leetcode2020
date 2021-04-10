class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dire = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = {}
        row, col = len(matrix), len(matrix[0])
        res = 0
        for i in range(row):
            for j in range(col):
                visited[(i,j)] = 0
        
        def dfs(i,j, mat):
            if visited[(i,j)] != 0:
                return visited[(i,j)] + 1
            for d in dire:
                nexti, nextj = i + d[0], j + d[1]
                if 0 <= nexti < len(mat) and 0 <= nextj < len(mat[0]) and mat[nexti][nextj] > mat[i][j]:
                    visited[(i,j)] = max(visited[(i,j)], dfs(nexti, nextj, mat))
            return visited[(i,j)] + 1
        
        for i in range(row):
            for j in range(col):
                res = max(res, dfs(i,j,matrix))
        return res