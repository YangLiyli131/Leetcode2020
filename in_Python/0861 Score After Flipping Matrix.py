class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for row in A:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]
        N = len(A[0])
        for i in range(N):
            if A[0][i] == 0:
                for j in range(len(A)):
                    A[j][i] = 1 - A[j][i]
        colsum = []
        for i in range(N):
            zeros = 0
            cur = 0
            for j in range(len(A)):
                if A[j][i] == 0:
                    zeros += 1
            if len(A) - zeros < zeros:
                for j in range(len(A)):
                    A[j][i] = 1 - A[j][i]
            for j in range(len(A)):
                cur += A[j][i]
            colsum.append(cur)
        res = 0
        p = 0
        while colsum:
            tmp = colsum.pop()
            res += tmp * (2 ** p)
            p += 1
        return res