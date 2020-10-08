class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        x = [1] * n
        x[0] = 0
        x[1] = 0
        i = 2
        while i*i < n:
            if x[i] == 0:
                i += 1
                continue
            j = i*i
            while j < n:
                x[j] = 0
                j += i
            i += 1
        return sum(x)
        