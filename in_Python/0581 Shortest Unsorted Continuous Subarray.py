class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = []
        for i in nums:
            n.append(i)
        n.sort()
        i = 0
        while i < len(n) and n[i] == nums[i]:
            i += 1
        j = len(n)-1
        while j >= 0 and n[j] == nums[j]:
            j -= 1
        return max(0, j - i + 1)