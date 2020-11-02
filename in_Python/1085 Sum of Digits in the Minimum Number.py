class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mini = 101
        for i in A:
            if i < mini:
                mini = i
        res = 0
        while mini:
            res += mini % 10
            mini /= 10
        if res % 2 == 0:
            return 1
        return 0