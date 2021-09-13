class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a,b = nums[0], nums[-1]
        for i in range(a,0,-1):
            if b % i == 0 and a % i == 0:
                return i
        return 1