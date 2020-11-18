class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        minute_angle = 6 * minutes
        base = 0
        if hour != 12:
            base = 30 * hour
        hour_angle = base + 30 * minutes / float(60)
        a = abs(hour_angle - minute_angle)
        return min(a, 360-a)
        