class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        d = {}
        for x in rectangles:
            c = min(x)
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        res = 0
        ma = 0
        for key in d:
            if key > ma:
                ma = key
                res = d[key]
        return res