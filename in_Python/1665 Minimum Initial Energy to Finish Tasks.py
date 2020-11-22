class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        total = 0
        maxeng = -sys.maxint
        dis = sys.maxint
        for t in tasks:
            total += t[0]
            d = t[1] - t[0]
            maxeng = max(maxeng, t[1])
            dis = min(d, dis)
        return max(maxeng, total + dis)