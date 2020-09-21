class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        diff = []
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                diff.append(1)
            elif A[i] == A[i-1]:
                diff.append(0)
            else:
                diff.append(-1)
        if 1 in diff and -1 in diff:
            return False
        return True