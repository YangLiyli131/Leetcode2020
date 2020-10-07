class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        s,e = 0,0
        counter = 0
        while e < len(A):
            if A[e] == 0:
                counter += 1
            while counter > K and s < len(A):
                if A[s] == 0:
                    counter -= 1
                s += 1
            res = max(res, e - s + 1)
            e += 1
        return res
        