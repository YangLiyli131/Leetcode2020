class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        N = len(nums)
        i,j = 0, N-1
        while i+1 < j:
            m = i + (j-i) / 2
            if nums[m] > target:
                j = m - 1
            elif nums[m] < target:
                i = m + 1
            else:
                j = m
        first = -1
        if nums[i] == target:
            first = i
        elif nums[j] == target:
            first = j
        i,j = 0, N-1
        while i+1 < j:
            m = i + (j-i) / 2
            if nums[m] > target:
                j = m - 1
            elif nums[m] < target:
                i = m + 1
            else:
                i = m   
        last = -1
        if nums[j] == target:
            last = j
        elif nums[i] == target:
            last = i
        if first == -1 or last == -1:
            return False
        if last - first + 1 > N/2:
            return True
        return False