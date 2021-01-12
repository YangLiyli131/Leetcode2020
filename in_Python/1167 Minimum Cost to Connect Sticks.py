class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        n = len(sticks)
        if n == 1:
            return 0
        hq = []
        for x in sticks:
            heapq.heappush(hq, x)
        res = 0
        while True:
            if len(hq) < 2:
                break
            a = heapq.heappop(hq)
            b = heapq.heappop(hq)
            c = a + b
            res += c
            heapq.heappush(hq, c)
        return res