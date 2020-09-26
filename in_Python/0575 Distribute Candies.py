class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        d = {}
        for c in candies:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        res = 0
        maxlen = len(candies) / 2
        for k in d:
            if d[k] > 0:
                d[k] -= 1
                res += 1
                if res == maxlen:
                    return maxlen
        return res
        