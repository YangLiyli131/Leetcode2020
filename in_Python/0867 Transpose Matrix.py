class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        
        m = row
        n = col
        a = [0] * n
        for i in range(n):
            a[i] = [0] * m
        for r in range(row):
            for c in range(col):
                a[c][r] = A[r][c]
        return a