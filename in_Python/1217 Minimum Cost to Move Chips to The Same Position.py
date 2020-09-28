class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        eve = 0
        odd = 0
        for p in position:
            if p % 2 == 0:
                eve += 1
            else:
                odd += 1
        return min(odd, eve)
        