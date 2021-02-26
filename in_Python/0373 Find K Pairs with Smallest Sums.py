class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        h = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                s = nums1[i] + nums2[j]
                heapq.heappush(h, [s, nums1[i], nums2[j]])
        r = []
        while k != 0 and h:
            k -= 1
            x = heapq.heappop(h)
            r.append([x[1],x[2]])
        return r