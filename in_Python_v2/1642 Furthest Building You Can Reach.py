class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        loc = []
        for i in range(len(heights)-1):
            d = heights[i+1] - heights[i]
            if d <= 0:
                continue
            heapq.heappush(loc, d)
            if len(loc) <= ladders:
                continue
            bricks -= heapq.heappop(loc)
            if bricks < 0:
                return i
        return len(heights)-1