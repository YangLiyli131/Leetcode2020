class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = 0
        i = 1
        while i < len(nums):
            if nums[i-1] > nums[i]:
                counter += 1
                if counter > 1:
                    return False
                if i == 1:
                    nums[i-1] = nums[i]
                else:
                    if nums[i] >= nums[i-2]:
                        nums[i-1] = nums[i]
                    else:
                        nums[i] = nums[i-1]
            i += 1
        return True
            
        