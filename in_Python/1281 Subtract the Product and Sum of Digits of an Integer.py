class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        res1 = 0
        res2 = 1
        while n != 0:
            res1 += n%10
            res2 *= n%10
            n /= 10

        return res2 - res1
        
        