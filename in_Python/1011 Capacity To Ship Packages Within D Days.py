class Solution(object):
    def able(self, weights, cap, D):
        used = 1
        cursum = 0
        for w in weights:
            if cursum + w > cap:
                used += 1
                cursum = 0
            cursum += w
        return used <= D
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        i = max(weights)
        j = sum(weights)
        while i < j:
            m = i + (j-i) / 2
            if self.able(weights, m, D):
                j = m
            else:
                i = m + 1
        return j