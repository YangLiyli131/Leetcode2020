class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        arr = [nums[0]]
        for i in range(1, len(nums)):
            arr.append(arr[-1] ^ nums[i])
        r = []
        for x in arr[::-1]:
            r.append(x ^ (2 ** maximumBit - 1 ))
        return r