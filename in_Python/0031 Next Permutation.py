class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = len(nums)-1
        locs = []
        while idx > 0:
            last = nums[idx]
            j = idx-1
            while j >= 0:
                if nums[j] >= last:
                    j -= 1
                else:
                    locs.append([j,idx])
                    break
            idx -= 1
        if len(locs) == 0:
            nums.sort()
            return
        ls = sorted(locs, key = lambda x : x[0], reverse = True)
        j = ls[0][0]
        idx = ls[0][1]

        t = nums[j]
        nums[j] = nums[idx]
        nums[idx] = t
        nums[j+1:] = sorted(nums[j+1:])
        