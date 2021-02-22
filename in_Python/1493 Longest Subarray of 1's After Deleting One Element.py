class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        if sum(nums) == 0:
            return 0
        if sum(nums) == len(nums):
            return len(nums)-1
        i,j = 0,0
        z = 0
        while j < len(nums):
            if nums[j] == 0:
                z += 1
            if z != 2:
                r = max(r, j-i)    
            if z == 2:       
                r = max(r, j-i-1)
                while i < len(nums) and nums[i] != 0:
                    i += 1
                i += 1
                z -= 1
            j += 1
        return r
            