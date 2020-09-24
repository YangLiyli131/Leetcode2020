class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 2:
            return min(cost[0], cost[1])
        dp = []
        dp.append(cost[0])
        dp.append(cost[1])
        for i in range(2, len(cost)-1):
            dp.append(min(dp[-1] + cost[i], dp[-2] + cost[i]))
        return min(dp[-1], dp[-2] + cost[-1])
        