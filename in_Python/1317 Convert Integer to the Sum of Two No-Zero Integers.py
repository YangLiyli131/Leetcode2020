class Solution(object):
    def check(self, n):
        while n != 0:
            if n % 10 == 0:
                return True
            n /= 10
        return False
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1, n):           
            if self.check(i):
                continue
            else:
                if not self.check(n-i):
                    return [i, n-i]
        return None
        