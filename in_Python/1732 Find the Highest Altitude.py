class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res = max(0, gain[0])
        for i in range(1, len(gain)):
            gain[i] = gain[i] + gain[i-1]
            res = max(res, gain[i])
        return res
        