class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        t = []
        t.append(0)
        t.append(1)
        if N == 0: return 0
        if N == 1: return 1
        for i in range(2,N+1):
            t.append(t[i-1]+t[i-2])
        return t[-1]
        