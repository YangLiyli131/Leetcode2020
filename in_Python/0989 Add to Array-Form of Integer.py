class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        res = []
        B = []
        while K != 0:
            B.insert(0, K % 10)
            K /= 10
        i = len(A)-1
        j = len(B)-1
        c = 0
        while i >= 0 and j >= 0:
            a = A[i]
            b = B[j]
            d = (a+b+c) % 10
            c = (a+b+c) / 10
            res.insert(0,d)
            i -= 1
            j -= 1
        while j >= 0:
            b = B[j]
            d = (b+c) % 10
            c = (b+c) / 10
            res.insert(0,d)
            j -= 1
        while i >= 0:
            a = A[i]
            d = (a+c) % 10
            c = (a+c) / 10
            res.insert(0,d)
            i -= 1
        if c == 1:
            res.insert(0,1)
        return res
                