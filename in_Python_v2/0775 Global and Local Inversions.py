class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i,x in enumerate(A):
            if abs(i - x) > 1:
                return False
        return True