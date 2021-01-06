class Solution(object):
    def merge(self, a, b):
        res = []
        i,j = 0,0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        while i < len(a):
            res.append(a[i])
            i += 1
        while j < len(b):
            res.append(b[j])
            j += 1
        return res
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        if len(nums) == 1:
            return [nums[0]]
        m = len(nums) // 2
        return self.merge(self.sortArray(nums[:m]), self.sortArray(nums[m:]))
        