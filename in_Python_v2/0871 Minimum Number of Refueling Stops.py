class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        dp = [startFuel] + [0] * len(stations)
        for i, (m, l) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= m:
                    dp[t+1] = max(dp[t+1], dp[t] + l)
        for i, d in enumerate(dp):
            if d >= target:
                return i
        return -1