class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        cursum = 0
        res = []
        for a in A:
            if a % 2 == 0:
                cursum += a
        for q in queries:            
            v = q[0]
            idx = q[1]
            old = A[idx]
            if v % 2 == 1 and old % 2 == 0:
                cursum -= old
            elif v % 2 == 1 and old % 2 == 1:
                cursum += old + v
            elif v % 2 == 0 and old % 2 == 0:
                cursum += v
            res.append(cursum)
            A[idx] += v
        return res