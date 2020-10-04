class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1 and nums[0] != target:
            return False
        i, j = 0, len(nums)-1
        while i < j and nums[i] == nums[i+1]:
            i += 1
        while i < j and nums[j] == nums[j-1]:
            j -= 1
        while i < j:
            m = i + (j-i) / 2
            if nums[m] == target or nums[i] == target or nums[j] == target:
                return True
            if nums[j] > target:
                if nums[m] >= nums[j]:
                    i = m + 1
                else:
                    if nums[m] > target:
                        j = m - 1
                    else:
                        i = m + 1
            elif nums[i] < target:
                if nums[m] <= nums[i]:
                    j = m - 1
                else:
                    if nums[m] > target:
                        j = m - 1
                    else:
                        i = m + 1
            else:
                return False
        return nums[i] == target