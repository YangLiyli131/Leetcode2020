class Solution(object):
    def minProductSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        a = sorted(nums1)
        b = sorted(nums2)
        i,j = 0, -1
        res = 0
        while i < len(a):
            res += a[i] * b[j]
            j -= 1
            i += 1
        return res