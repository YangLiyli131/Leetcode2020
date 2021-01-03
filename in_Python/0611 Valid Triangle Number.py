class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for i in range(len(nums)-1, -1, -1):
            cur = nums[i]
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > cur:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res
            