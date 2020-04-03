class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        i,j = 0,len(A)-1
        p = len(A)
        while p != 0:
            if A[i] **2 < A[j] **2:
                res.insert(0,A[j]**2)
                j -= 1
            else:
                res.insert(0,A[i]**2)
                i += 1
            p -= 1
        return res