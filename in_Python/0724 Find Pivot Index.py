class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum = []
        rightsum = []
        if nums == None or len(nums) == 0:
            return -1
        leftsum.append(nums[0])
        rightsum.append(nums[-1])
        for i in range(1, len(nums)):
            leftsum.append(leftsum[i-1] + nums[i])
            rightsum.append(rightsum[i-1] + nums[len(nums)-1-i])
        for i in range(len(nums)):
            if leftsum[i] == rightsum[len(nums)-1-i]:
                return i
        return -1