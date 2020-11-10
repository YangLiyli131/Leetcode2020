class Solution(object):
    def isP(self, n):
        if n <= 1:
            return False
        for i in range(2,n/2+1):
            if n % i == 0:
                return False
        return True
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        o = 0
        e = 0
        for i in range(1, n+1):
            if self.isP(i):
                o += 1
            else:
                e += 1
        res = 1
        while o != 0:
            res *= o
            o -= 1
        while e != 0:
            res *= e
            e -= 1
        return res % (pow(10,9)+7)