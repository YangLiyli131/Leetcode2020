class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.sort()
        verticalCuts.sort()
        mh, mv = horizontalCuts[0], verticalCuts[0]
        for i in range(1, len(horizontalCuts)):
            c = horizontalCuts[i] - horizontalCuts[i-1]
            mh = max(mh, c)
        for i in range(1, len(verticalCuts)):
            c = verticalCuts[i] - verticalCuts[i-1]
            mv = max(mv, c)
        mh = max(mh, h - horizontalCuts[-1])
        mv = max(mv, w - verticalCuts[-1])
        return (mh * mv) % 1000000007