class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        da = {}
        db = {}
        rowa = len(A)
        rowb = len(B)
        cola = len(A[0])
        colb = len(B[0])
        for i in range(rowa):
            for j in range(cola):
                if A[i][j] != 0:
                    da[(i,j)] = A[i][j]
        for i in range(rowb):
            for j in range(colb):
                if B[i][j] != 0:
                    db[(i,j)] = B[i][j]
        r = []
        for i in range(rowa):
            r.append([0] * colb)
        for k in da:
            curi, curj = k[0], k[1]
            for kk in db:
                if curj == kk[0]:
                    newi = k[0]
                    newj = kk[1]
                    r[newi][newj] += da[k] * db[kk]
        return r