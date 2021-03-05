class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        f = [1,1]
        cur = 2
        while cur <= k:
            f.append(cur)
            cur = f[-1] + f[-2]
        r = 0
        while k != 0:
            k -= f[-1]
            r += 1
            while f and f[-1] > k:
                f.pop()
        return r