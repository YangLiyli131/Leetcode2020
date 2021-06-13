class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        s = set()
        for x in ranges:
            for y in range(x[0], x[1]+1):
                s.add(y)
        for x in range(left, right+1):
            if x not in s:
                return False
        return True