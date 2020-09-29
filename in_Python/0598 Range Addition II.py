class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        rowmin = m
        colmin = n
        for o in ops:
            a = o[0]
            b = o[1]
            rowmin = min(a, rowmin)
            colmin = min(b, colmin)
        return rowmin * colmin
            
        