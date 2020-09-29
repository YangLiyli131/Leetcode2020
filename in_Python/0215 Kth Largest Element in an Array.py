class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = []
        for i in nums:
            heappush(q, i)
        while len(q) > k:
            heappop(q)
        return heappop(q)