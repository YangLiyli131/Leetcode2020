class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        curmax = heights[-1]
        r = []
        r.append(len(heights)-1)
        for i in range(len(heights)-2, -1, -1):
            curh = heights[i]
            if curh > curmax:
                curmax = curh
                r.append(i)
        return r[::-1]