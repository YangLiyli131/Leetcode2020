class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in nums:
            c = x % 10
            x /= 10
            b = x % 10
            a = x / 10
            d[(a,b)] = c
        r = 0
        for x in nums:
            c = x % 10
            x /= 10
            b = x % 10
            a = x / 10
            if (a+1, 2*b-1) in d:
                d[(a+1, 2*b-1)] += d[(a,b)]
            if (a+1, 2*b) in d:
                d[(a+1, 2*b)] += d[(a,b)]
            if (a+1, 2*b-1) not in d and (a+1, 2*b) not in d:
                r += d[(a,b)]
        return r