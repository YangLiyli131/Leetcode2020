class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        res = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ones_on_bound = []
        row = len(A)
        col = len(A[0])
        for i in [0,row-1]:
            for j in range(col):
                if A[i][j] == 1:
                    ones_on_bound.append([i,j])
        for j in [0, col-1]:
            for i in range(row):
                if A[i][j] == 1 and [i,j] not in ones_on_bound:
                    ones_on_bound.append([i,j])
        while len(ones_on_bound) != 0:
            n = ones_on_bound.pop(0)
            thisi = n[0]
            thisj = n[1]
            A[thisi][thisj] = -1
            for d in directions:
                nexti = thisi + d[0]
                nextj = thisj + d[1]
                if 0 < nexti < row and 0 < nextj < col and A[nexti][nextj] == 1:
                    ones_on_bound.append([nexti,nextj])
                    A[nexti][nextj] = -1
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    res += 1
        return res