class Solution(object):
    def helper(self, t):
        temp = 0
        while t != 0:
            t /= 10
            temp += 1
        return temp % 2 == 0
    
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for x in nums:
            if self.helper(x):
                res += 1
        return res

        