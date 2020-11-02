class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        r = 0
        NN = N
        n = len(str(N))
        while N != 0:
            x = N % 10
            r += pow(x, n)
            N /= 10
        return r == NN