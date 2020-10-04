class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = -1
        i, j = 0, len(nums)-1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while i < j:
            m = i + (j-i) / 2
            if nums[m] == target:
                return m
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if nums[j] > target:
                if nums[m] > nums[j]:
                    i = m + 1
                else:
                    if nums[m] < target:
                        i = m + 1
                    else:
                        j = m - 1
                continue
            elif nums[i] < target:
                if nums[m] < nums[i]:
                    j = m - 1
                else:
                    if nums[m] < target:
                        i = m + 1
                    else:
                        j = m - 1
                continue
            else:
                return -1
        return res