class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 1
        hp = []
        for i in nums:
            if i > 0:
                heapq.heappush(hp,i)
        if not hp or len(hp) == 0:
            return 1
        pre = heapq.heappop(hp)
        if pre > 1:
            return 1
        r = -1
        while hp:
            cur = heapq.heappop(hp)
            if cur - pre > 1:
                r = pre + 1
                break
            pre = cur
        if r == -1:
            r = pre + 1
        return r