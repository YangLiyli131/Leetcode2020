class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        idx = m + n - 1
        while i >= 0 and j >= 0:
            a = nums1[i]
            b = nums2[j]
            if a < b:
                nums1[idx] = b
                idx -= 1
                j -= 1
            elif a > b:
                nums1[idx] = a
                idx -= 1
                i -= 1
            else:
                nums1[idx] = a
                nums1[idx-1] = b
                i -= 1 
                j -= 1
                idx -= 2
        while i >= 0:
            nums1[idx] = nums1[i]
            i -= 1
            idx -= 1
        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1
        