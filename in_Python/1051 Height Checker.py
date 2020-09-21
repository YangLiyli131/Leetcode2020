class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h = []
        for hh in heights:
            h.append(hh)
        h.sort()
        res = 0
        for i in range(len(h)):
            if h[i] != heights[i]:
                res += 1
        return res