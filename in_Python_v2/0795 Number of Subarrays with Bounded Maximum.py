class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        def count(B):
            ans = cur = 0
            for x in nums:
                if x <= B:
                    cur += 1
                else:
                    cur = 0
                ans += cur
            return ans
        return count(right) - count(left-1)