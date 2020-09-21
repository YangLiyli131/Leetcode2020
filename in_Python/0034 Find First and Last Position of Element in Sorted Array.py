class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        res = []
        res.append(-1)
        res.append(-1)
        if nums == None or len(nums) == 0:
            return res
        while i < j:
            m = i + (j-i)/2
            if nums[m] < target:
                i = m + 1
            else:
                j = m
        if nums[i] == target:
            res[0] = i
        i = 0
        j = len(nums) - 1
        while i+1 < j:
            m = i + (j-i)/2
            if nums[m] > target:
                j = m - 1
            elif nums[m] == target:
                i = m
            else:
                i = m + 1
        if nums[j] == target:
            res[1] = j
        elif nums[i] == target:
            res[1] = i           
        return res