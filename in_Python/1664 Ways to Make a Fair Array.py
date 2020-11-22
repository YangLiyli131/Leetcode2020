class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_odd = {}
        left_even = {}
        right_odd = {}
        right_even = {}
        arr = nums[:]
        left_even_cum = 0
        left_odd_cum = 0
        for i in range(len(nums)):
            left_odd[i] = left_odd_cum
            left_even[i] = left_even_cum
            if i % 2 == 0:
                left_even_cum += nums[i]
            else:
                left_odd_cum += nums[i]
        right_odd_cum = 0
        right_even_cum = 0
        for i in range(len(nums)-1, -1, -1):
            right_odd[i] = right_odd_cum
            right_even[i] = right_even_cum
            if i % 2 == 0:
                right_even_cum += nums[i]
            else:
                right_odd_cum += nums[i]
        res = 0
        for i in range(len(nums)):
            if left_even[i] + right_odd[i] == left_odd[i] + right_even[i]:
                    res += 1
        return res