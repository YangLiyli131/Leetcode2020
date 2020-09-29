class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        residuals = []
        for i in range(60):
            residuals.append(0)
        for t in time:
            r = t % 60
            residuals[r] += 1
        n = residuals[0]
        #print(residuals)
        res = n * (n-1) / 2
        i = 1
        j = 59
        while i < j:
            a = residuals[i]
            b = residuals[j]
            res += a * b
            i += 1
            j -= 1
        res += residuals[30] * (residuals[30]-1) / 2
        return res