class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        cur = [0]
        for i in range(len(A)):
            cur.append(cur[-1] + A[i])
        i = L
        Larr = []
        while i < len(cur):
            Ls = cur[i] - cur[i-L]
            Larr.append([i-L+1, i, Ls])
            i += 1
        Marr = []
        i = M
        while i < len(cur):
            Ms = cur[i] - cur[i-M]
            Marr.append([i-M+1, i, Ms])
            i += 1
        r = 0
        def check(a,b,x,y):
            return b < x or a > y
        for x in Larr:
            a,b,c = x[0],x[1],x[2]
            for y in Marr:
                aa,bb,cc = y[0],y[1],y[2]
                if check(a,b,aa,bb):
                    r = max(r, c + cc)
        return r
            
        