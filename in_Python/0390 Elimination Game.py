class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def h(n, f):
            if n == 1:
                return 1
            if f:
                return 2 * h(n/2, 0)
            elif n % 2 == 1:
                return 2 * h(n/2, 1)
            else:
                return 2 * h(n/2, 1) - 1
        return h(n,1)