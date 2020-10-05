class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = []
        for i in nums:
            t.append(0)
        for i in range(len(nums)):
            cur = nums[i]
            if t[cur] == -1:
                return cur
            t[cur] = -1
        return 0