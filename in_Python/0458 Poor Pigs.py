class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        res = 0
        while (minutesToTest / minutesToDie + 1) ** res < buckets:
            res += 1
        return res