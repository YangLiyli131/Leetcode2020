class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        inc = False
        dec = False
        i = 0
        while i < len(A):
            j = i + 1
            while j < len(A) and A[j] > A[j-1]:
                j += 1
                inc = True
            if not inc:
                i = j
                continue
            while j < len(A) and A[j] < A[j-1]:
                j += 1
                dec = True
            if not dec:
                i = j
                inc = False
                continue
            res = max(res, j-i)
            i += 1
        return res