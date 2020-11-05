class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        row = len(A)
        col = len(A[0])
        mat = []
        for i in range(row):
            mat.append(list(A[i]))
        res = 0
        for j in range(col):
            for i in range(1, row):
                if mat[i][j] < mat[i-1][j]:
                    res += 1
                    break
        return res