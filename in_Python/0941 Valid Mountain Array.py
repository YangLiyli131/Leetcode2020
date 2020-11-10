class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i,j = 0, len(A)-1
        while i < len(A)-1:
            if A[i+1] > A[i]:
                i += 1
            else:
                break
        while j > 0:
            if A[j-1] > A[j]:
                j -= 1
            else:
                break
        return i != 0 and j != len(A)-1 and i == j