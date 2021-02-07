class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        r = 0
        hp = []
        heapq.heappush(hp,-a)
        heapq.heappush(hp,-b)
        heapq.heappush(hp,-c)
        while len(hp) > 1:
            x = -heapq.heappop(hp)
            y = -heapq.heappop(hp)
            x -= 1
            y -= 1
            r += 1
            if x != 0:
                heapq.heappush(hp,-x)
            if y != 0:
                heapq.heappush(hp,-y)
        return r