class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        r = 0
        for i in range(1,len(timeSeries)):
            c = timeSeries[i] - timeSeries[i-1]
            if c > duration:
                r += duration
            else:
                r += c
        return r + duration