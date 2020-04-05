class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = []
        left.append(1)
        for i in range(1,len(nums)):
            left.append(left[i-1] * nums[i-1])
            
        right = []
        for i in range(len(nums)-1): right.append(0)
        right.append(1)

        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        res = []
        for i in range(len(left)):
            res.append(left[i] * right[i])
        return res