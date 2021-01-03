class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        res = 0
        for i in range(len(nums)):
            cur = nums[i]
            j,k = i+1, len(nums)-1
            while j < k:
                if cur + nums[j] + nums[k] < target:
                    res += k - j
                    j += 1
                else:
                    k -= 1
        return res