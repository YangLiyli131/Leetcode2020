class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = set()
        b = set()
        for i in nums1:
            a.add(i)
        for i in nums2:
            b.add(i)
        res = []
        for i in a:
            if i in b:
                res.append(i)
        return res