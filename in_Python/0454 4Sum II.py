class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res = 0
        d1 = {}
        d2 = {}
        N = len(A)
        for i in range(N):
            a = A[i]
            for j in range(N):
                b = B[j]
                t = a + b
                if t in d1:
                    d1[t] += 1
                else:
                    d1[t] = 1
        for i in range(N):
            a = C[i]
            for j in range(N):
                b = D[j]
                t = a + b
                if t in d2:
                    d2[t] += 1
                else:
                    d2[t] = 1
        for k in d1:
            if -k in d2:
                res += d1[k] * d2[-k]
        return res