class Solution(object):
    def rev(self, arr, i, j):
        while i < j:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
            i += 1
            j -= 1
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.rev(nums,0,len(nums)-k-1)
        self.rev(nums,len(nums)-k,len(nums)-1)
        self.rev(nums,0,len(nums)-1)
