class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def check(x):
            for i in range(1, len(x)):
                if x[i] <= x[i-1]:
                    return False
            return True
        for i in range(len(nums)):
            nn = nums[:i] + nums[i+1:]
            if nn == sorted(nn) and check(nn):
                return True
        return False