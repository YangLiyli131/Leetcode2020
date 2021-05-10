class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        arr = [0] * (2050 - 1950 + 1)
        for x in logs:
            a,b = x[0]-1950, x[1]-1950
            for i in range(a,b):
                arr[i] += 1
        m = max(arr)
        for i,x in enumerate(arr):
            if x == m:
                return i+1950
        return 0