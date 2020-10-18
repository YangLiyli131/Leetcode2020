class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            cur = nums[i]
            j = i-1
            while j >= 0 and nums[j] > cur:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = cur
        return nums

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = 0
        for i in nums:
            if i == 0:
                a += 1
            elif i == 1:
                b += 1
            else:
                c += 1
        idx = 0
        while a != 0:
            a -= 1
            nums[idx] = 0
            idx += 1
        while b != 0:
            b -= 1
            nums[idx] = 1
            idx += 1
        while c != 0:
            c -= 1
            nums[idx] = 2
            idx += 1
