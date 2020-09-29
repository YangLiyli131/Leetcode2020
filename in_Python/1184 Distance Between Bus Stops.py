class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        ss = 0
        for i in distance:
            ss += i
        s = 0
        a = min(start,destination)
        b = max(start,destination)
        for i in range(a,b):
            s += distance[i]
        return min(s, ss-s)