class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        diff = nums[-1] - nums[0] + 1
        miss = diff - len(nums)
        if k > miss:
            return nums[-1] + k - miss
        i,j = 0, len(nums)-1
        while i +1 < j:
            m = i + (j-i) / 2
            mis = nums[m] - nums[i] - (m-i)
            if mis < k:
                i = m 
                k -= mis
            else:
                j = m
        return nums[i] + k
            